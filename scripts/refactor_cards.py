import re

def refactor_cards(content):
    # Regex to find Megami sections and their card divs
    pattern = r'## (.*?)\n\n<div style="display: flex; flex-wrap: wrap; gap: 10px;">(.*?)</div>'
    
    def replacer(match):
        megami = match.group(1)
        cards_html = match.group(2).strip()
        
        # Extract individual links
        links = re.findall(r'<a href="(.*?)" class="glightbox"><img src="(.*?)" width="150" alt="(.*?)"></a>', cards_html)
        
        new_content = f'## {megami}\n\n'
        new_content += '<div class="grid cards" markdown>\n\n'
        for href, src, alt in links:
            new_content += f'-   [:external-link: ![{alt}]({src})]({href}){{ .glightbox }}\n\n'
        new_content += '</div>'
        return new_content

    return re.sub(pattern, replacer, content, flags=re.DOTALL)

with open('/home/kafka/furuyoni/docs/megami/cards.md', 'r') as f:
    content = f.read()

new_content = refactor_cards(content)

with open('/home/kafka/furuyoni/docs/megami/cards.md', 'w') as f:
    f.write(new_content)
