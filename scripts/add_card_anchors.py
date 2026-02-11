
import os
import re

card_file = "/home/kafka/furuyoni/docs/megami/cards.md"

with open(card_file, "r") as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    stripped = line.strip()
    # Logic: Card name is indented by 4 spaces and is the line after a list item (image)
    # The image line starts with "- " and contains "[:external-link: ![" usually
    
    if i > 0:
        prev_line = lines[i-1].strip()
        if prev_line.startswith("- ") and "[:external-link:" in prev_line:
            # Current line looks like "    CardName"
            # It might be empty if the image line is separated by newline? Usually not in this file based on view.
            
            if line.startswith("    ") and not stripped.startswith("-") and stripped:
                # Extract text
                # Handle existing attributes if any
                base_text = stripped.split("{")[0].strip()
                
                # Create ID
                # Japanese text as ID is fine generally.
                new_line = f"    {base_text} {{: #{base_text} }}\n"
                new_lines.append(new_line)
                continue

    new_lines.append(line)

with open(card_file, "w") as f:
    f.writelines(new_lines)

print(f"Updated {card_file} with anchors.")
