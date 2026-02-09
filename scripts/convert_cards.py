import re
import yaml
import json
from typing import Dict, List

def load_config(config_path: str) -> Dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def main() -> None:
    config: Dict = load_config("config.yaml")
    data_js_path: str = config["paths"]["data_js"]
    base_url: str = config["urls"]["base_card_url"]
    output_path: str = config["paths"]["output_cards"]

    with open(data_js_path, "r", encoding="utf-8") as f:
        content: str = f.read()

    start_idx: int = content.find("export const cards = {") + len("export const cards = {")
    end_idx: int = content.find("};", start_idx)
    cards_str: str = "{" + content[start_idx:end_idx].strip() + "}"
    cards_str = cards_str.replace("'", '"')
    cards_str = re.sub(r",\s*([}\]])", r"\1", cards_str)
    
    cards_data: Dict[str, List[str]] = json.loads(cards_str)

    output: str = "# メガミカードギャラリー\n\n各メガミの通常札一覧です。画像をクリックすると拡大表示されます。\n\n"

    for megami, card_paths in cards_data.items():
        output += f"## {megami}\n\n"
        output += '<div style="display: flex; flex-wrap: wrap; gap: 10px;">\n'
        for path in card_paths:
            full_url: str = f"{base_url}{path}"
            output += f'  <a href="{full_url}" class="glightbox"><img src="{full_url}" width="150" alt="{megami} Card"></a>\n'
        output += "</div>\n\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)

if __name__ == "__main__":
    main()
