import re
import os

def refactor_markdown(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Find sequences of <img ... alt="Card"> or similar
    # In curriculum, it looks like: **Megami Cards:**\n\n<img ...> <img ...>
    # In pairs, it's inside <details>
    
    img_pattern = r'<img src="(.*?)" width="(\d+)" alt="(.*?)">'
    
    def grid_replacer(match):
        imgs_block = match.group(0)
        imgs = re.findall(img_pattern, imgs_block)
        if not imgs:
            return imgs_block
        
        new_block = '<div class="grid cards" markdown>\n\n'
        for src, width, alt in imgs:
            # We skip the width and use grid
            new_block += f'-   ![{alt}]({src})\n\n'
        new_block += '</div>'
        return new_block

    # Refactor blocks of images
    # Look for groups of 2 or more images
    block_pattern = r'(?:<img src=".*?" width="\d+" alt=".*?">\s*){2,}'
    new_content = re.sub(block_pattern, grid_replacer, content)

    with open(file_path, 'w') as f:
        f.write(new_content)

refactor_markdown('/home/kafka/furuyoni/docs/beginner/curriculum.md')
refactor_markdown('/home/kafka/furuyoni/docs/pairs/index.md')
