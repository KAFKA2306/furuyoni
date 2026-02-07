import json

# Manually defining because reading data.js directly is tricky without a JS parser
# But I can extract it since it's simple
data_js_path = '/home/kafka/furuyoni/data.js'
base_url = "https://main-bakafire.ssl-lolipop.jp/furuyoni/na/"

with open(data_js_path, 'r') as f:
    content = f.read()

# Very basic extraction of cards object
# Look for 'export const cards = {' and '};'
start_idx = content.find('export const cards = {') + len('export const cards = {')
end_idx = content.find('};', start_idx)
cards_str = '{' + content[start_idx:end_idx].strip() + '}'

# Clean up trailing commas and other non-JSON things
# Replace single quotes with double quotes
cards_str = cards_str.replace("'", '"')
# Remove trailing commas before closing braces/brackets
import re
cards_str = re.sub(r',\s*([}\]])', r'\1', cards_str)

import json
cards_data = json.loads(cards_str)

output = "# メガミカードギャラリー\n\n"
output += "各メガミの通常札一覧です。画像をクリックすると拡大表示されます。\n\n"

for megami, card_paths in cards_data.items():
    output += f"## {megami}\n\n"
    output += '<div style="display: flex; flex-wrap: wrap; gap: 10px;">\n'
    for path in card_paths:
        full_url = f"{base_url}{path}"
        output += f'  <a href="{full_url}" class="glightbox"><img src="{full_url}" width="150" alt="{megami} Card"></a>\n'
    output += '</div>\n\n'

with open('/home/kafka/furuyoni/docs/megami/cards.md', 'w') as f:
    f.write(output)

print("docs/megami/cards.md has been generated.")
