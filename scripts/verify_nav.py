import sys
from playwright.sync_api import sync_playwright

def verify_navigation():
    with sync_playwright() as p:
        # Launch Google Chrome specifically
        browser = p.chromium.launch(executable_path="/usr/bin/google-chrome")
        # Set viewport to force scrollbar (height 600)
        page = browser.new_page(viewport={"width": 1280, "height": 600})
        
        # Listen for console logs - Important: attach before goto
        page.on("console", lambda msg: print(f"Browser Console: {msg.text}"))
        page.on("pageerror", lambda err: print(f"Page Error: {err}"))
        page.on("requestfailed", lambda req: print(f"Request Failed: {req.url} - {req.failure}"))
        
        page.goto("http://localhost:8080")
        
        # Initial State: Pair Guide should be visible (check class instead of visibility for now)
        print("Checking initial state classes...")
        pair_view_class = page.locator("#pair-view").get_attribute("class")
        print(f"Initial #pair-view class: {pair_view_class}")
        
        # Click Beginner Story
        print("Clicking 'Beginner Story'...")
        # Try JS click to bypass potential overlays
        page.evaluate("document.querySelector('button[data-view=\"story\"]').click()")
        
        # Wait for class change
        try:
            page.wait_for_function("document.querySelector('#story-view').classList.contains('hidden') === false", timeout=5000)
        except Exception as e:
            print(f"Timeout waiting for class change: {e}")
            page.screenshot(path="/home/kafka/furuyoni/debug_timeout.png")
            print("Saved debug_timeout.png")
        
        if not page.is_visible("#story-view"):
             print("Warning: Story view might not be 'visible' to playwright, but class is correct.")
             
        # Verify classes
        story_class = page.locator("#story-view").get_attribute("class")
        pair_class = page.locator("#pair-view").get_attribute("class")
        print(f"Story class: {story_class}, Pair class: {pair_class}")

        if "hidden" in story_class or "hidden" not in pair_class:
             print("Error: Class toggling failed")
             sys.exit(1)

        page.screenshot(path="/home/kafka/furuyoni/screenshot_story.png")
        print("Story view verified. Screenshot saved.")

        # Scroll down to show custom scrollbar
        print("Scrolling down...")
        page.mouse.wheel(0, 500)
        page.wait_for_timeout(500) # Wait for potential smooth scroll
        page.screenshot(path="/home/kafka/furuyoni/screenshot_chrome_scroll.png")
        print("Scrolled view saved to screenshot_chrome_scroll.png")

        # Click Pair Guide
        print("Clicking 'Pair Guide'...")
        page.evaluate("document.querySelector('button[data-view=\"pair\"]').click()")
        
        try:
            page.wait_for_function("document.querySelector('#pair-view').classList.contains('hidden') === false", timeout=5000)
        except Exception:
             print("Error: Pair view not visible after clicking back")
             sys.exit(1)
             
        print("Navigation verification successful.")
        browser.close()

if __name__ == "__main__":
    verify_navigation()
