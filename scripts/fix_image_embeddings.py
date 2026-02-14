import os
import re

def fix_files(directory):
    # Regex for standalone horizontal rule replacement:
    # Pattern: [![---](...na_14_o_n_7.png)](...){ .glightbox } or similar variations
    # We want to be careful to catch the exact pattern observed in the files.
    # Observed in beginner.md: [![---](assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }
    
    # We will look for the image filename specifically in the context of what looks like a horizontal rule replacement.
    
    # Pattern 1: Standalone HR replacement
    # matches: [![---](path/to/na_14_o_n_7.png)](path/to/na_14_o_n_7.png){ .glightbox }
    hr_pattern = re.compile(r'\[!\[---\]\(.*?na_14_o_n_7\.png\)\].*?\{ \.glightbox \}')

    # Pattern 2: Table separator replacements
    # The user mentioned "table separators". 
    # Standard table separator line looks like: | :--- | :---: | ---: |
    # If it was replaced, it might look like: | :[![---](...)...] | ...
    
    # We'll just replace the specific image link string back to "---" if it occurs inside a table context or looks like it was meant to be a separator.
    # However, since the image link is quite long, simple substitution of the whole link block with "---" might work for most cases.
    
    # Let's define the specific "bad string" we want to kill.
    # It seems consistent: [![---](assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }
    # Or with relative paths.
    
    # Strategy:
    # 1. Read file.
    # 2. Re.sub the specific bad block with "---".
    # 3. Handle edge cases where "---" needs to be ":---" or ":---:" or "---:" 
    #    But if the original was "---" and it got replaced by the image markdown, 
    #    reverting it to "---" *should* often be enough if the colons were preserved outside the match.
    #    Wait, if the regex matched `---` and replaced it, the colons might still be there.
    #    Let's check `docs/megami/01_yurina.md` line 49 from the previous turn:
    #    | :[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](...){ .glightbox } | ...
    #    Here we see the colon `:` IS preserved before the image link.
    #    So replacing the image link block with `---` should perfectly restore `:---`.
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not file.endswith(".md"):
                continue
            
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # The pattern is basically: 
            # [![---]( <URL> )]( <URL> ){ .glightbox }
            # where <URL> contains na_14_o_n_7.png
            
            # Regex:
            # \[!\[---\]\(.*?\)\].*?\{ \.glightbox \}
            # We restrict it to containing na_14_o_n_7.png
            
            pattern = re.compile(r'\[!\[---\]\([^)]*?na_14_o_n_7\.png\)\].*?\{ \.glightbox \}')
            
            if pattern.search(content):
                print(f"Fixing {path}...")
                new_content = pattern.sub('---', content)
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

if __name__ == "__main__":
    fix_files("/home/kafka/furuyoni/docs")
