# User Stories - Furuyoni Pair Guide

## Personas

1.  Beginner Player (Akane)
    *   Has just started playing Furuyoni or played a few games.
    *   Overwhelmed by the number of goddesses (Megaemis) and possible combinations.
    *   Wants to find a pair that is easy to play and strong enough to learn the basics.
    *   Needs step-by-step guidance.

2.  Intermediate Player (Ren)
    *   Understands basic rules but wants to try new pairs.
    *   Looking for specific playstyles (Control, Aggro, Combo).
    *   Needs detailed information on strengths, weaknesses, and key cards.

3.  Developer (Kaito)
    *   Maintains the application.
    *   Wants the code to be clean, modular, and easy to update as new seasons/expansions are released.

---

## Epics & Stories

### Epic 1: Pair Discovery (The "Pair Guide" View)
*Goal: Allow players to explore and understand differnet goddess combinations.*

*   US-1.1: Browse All Pairs
    *   As a player (Akane/Ren),
    *   I want to see a grid of all recommended beginner pairs,
    *   So that I can get an overview of the options available to me.
    *   *Acceptance Criteria:*
        *   Displays a responsive grid of pair cards.
        *   Each card shows the names of the two goddesses and a brief tagline.

*   US-1.2: View Pair Details
    *   As a player,
    *   I want to click on a pair to see detailed information,
    *   So that I can understand how that specific pair plays.
    *   *Acceptance Criteria:*
        *   Opens a modal or detail view.
        *   Shows: Description, Strengths (Pros), Weaknesses (Cons).
        *   Shows: Key cards for each goddess.

*   US-1.3: Inspect Cards
    *   As a player,
    *   I want to see the card images for each goddess in the pair,
    *   So that I know which cards to put in my deck.
    *   *Acceptance Criteria:*
        *   Clicking a card thumbnail opens/zooms the full card image (or links to the official site).

### Epic 2: Structured Learning (The "Beginner Story" View)
*Goal: Guide beginners through a curriculum of pairs to learn concepts incrementally.*

*   US-2.1: Follow a Learning Path
    *   As a Beginner Player (Akane),
    *   I want to see a numbered list of "Story Steps",
    *   So that I know which pair to try first, second, and so on.
    *   *Acceptance Criteria:*
        *   A timeline or list view numbered 1 to 10.
        *   Each step has a Title, Subtitle, and Learning Goals ("Lessons").

*   US-2.2: Focus on a Story Pair
    *   As a Beginner Player,
    *   I want a "Focus Pair Detail" button on each story step,
    *   So that I can quickly jump to the details of the specific pair recommended for that lesson.
    *   *Acceptance Criteria:*
        *   Clicking the button opens the Pair Detail modal for the relevant pair.

### Epic 3: User Experience & Performance
*Goal: Ensure the application is pleasant and accessible.*

*   US-3.1: Responsive Design
    *   As a player,
    *   I want to access the guide on my smartphone while at a card shop,
    *   So that I can look up strategies during a game session.
    *   *Acceptance Criteria:*
        *   Layout adjusts for mobile screens (single column) vs desktop (grid/sidebar).

*   US-3.2: Fast Loading
    *   As a player,
    *   I want the images to load quickly or lazily,
    *   So that I don't waste data or wait long for the page to render.
    *   *Acceptance Criteria:*
        *   Images implement `loading="lazy"`.

### Epic 4: Maintainability (Technical)
*Goal: Keep the project healthy.*

*   US-4.1: Static Asset Management
    *   As a Developer (Kaito),
    *   I want to separate the source code (`src/`) from the build/public root,
    *   So that the project structure is clean.
    *   *(Note: This was addressed by the recent refactor).*

*   US-4.2: Data-Driven Content
    *   As a Developer,
    *   I want pairs and stories to be defined in JavaScript objects/JSON,
    *   So that I can add new pairs without writing new HTML structures manually.
    *   *Acceptance Criteria:*
        *   `data.js` and `story.js` contain the content.
        *   `main.js` renders the HTML dynamically.
