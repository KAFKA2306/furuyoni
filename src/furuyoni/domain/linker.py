from pathlib import Path
import re
from typing import Dict, List, Optional
from furuyoni.infrastructure.paths import DOCS_DIR, get_relative_path

TERM_MAPPING: Dict[str, str] = {
    "ユリナ": "megami/index.md",
    "サイネ": "megami/index.md",
    "ヒミカ": "megami/index.md",
    "トコヨ": "megami/index.md",
    "オボロ": "megami/index.md",
    "ユキヒ": "megami/index.md",
    "シンラ": "megami/index.md",
    "ハガネ": "megami/index.md",
    "チカゲ": "megami/index.md",
    "クルル": "megami/index.md",
    "サリヤ": "megami/index.md",
    "ライラ": "megami/index.md",
    "ウツロ": "megami/index.md",
    "ホノカ": "megami/index.md",
    "コルヌ": "megami/index.md",
    "ヤツハ": "megami/index.md",
    "桜花結晶": "mechanics/index.md",
    "ライフ": "mechanics/index.md",
    "オーラ": "mechanics/index.md",
    "フレア": "mechanics/index.md",
    "間合": "mechanics/index.md",
    "ダスト": "mechanics/index.md",
    "集中力": "mechanics/index.md",
    "通常札": "mechanics/index.md",
    "切札": "mechanics/index.md",
    "終焉影": "mechanics/index.md",
    "前進": "mechanics/index.md",
    "後退": "mechanics/index.md",
    "纏い": "mechanics/index.md",
    "宿し": "mechanics/index.md",
    "開始フェイズ": "mechanics/flow.md",
    "メインフェイズ": "mechanics/flow.md",
    "終了フェイズ": "mechanics/flow.md",
    "再構成": "mechanics/flow.md",
    "眼前構築": "mechanics/flow.md",
    "双掌繚乱": "mechanics/flow.md",
    "連火": "mechanics/index.md",
    "決死": "mechanics/index.md",
    "八相": "mechanics/index.md",
    "境地": "mechanics/index.md",
    "設置": "mechanics/index.md",
    "開閉": "mechanics/index.md",
    "計略": "mechanics/index.md",
    "遠心": "mechanics/index.md",
    "毒": "megami/index.md",
    "機巧": "mechanics/index.md",
    "騎動": "mechanics/index.md",
    "造花": "mechanics/index.md",
    "帯電": "mechanics/index.md",
    "灰塵": "mechanics/index.md",
    "守護": "mechanics/index.md",
    "凍結": "mechanics/index.md",
    "鏡映": "mechanics/index.md",
}

class Linker:
    def __init__(self, mapping: Dict[str, str] = TERM_MAPPING) -> None:
        self.mapping: Dict[str, str] = mapping
        self.sorted_terms: List[str] = sorted(mapping.keys(), key=len, reverse=True)
        self.pattern: re.Pattern = self._build_pattern()

    def _build_pattern(self) -> re.Pattern:
        p_link: str = r'\[.*?\]\(.*?\)'
        p_image: str = r'!\[.*?\]\(.*?\)'
        p_code_inline: str = r'`[^`\n]+`'
        p_code_block: str = r'```[\s\S]*?```'
        p_html: str = r'<[^>]+>'
        p_header: str = r'^#{1,6}\s.*$'
        protected_pattern: str = f"({p_code_block}|{p_link}|{p_image}|{p_code_inline}|{p_html}|{p_header})"
        terms_pattern: str = "(" + "|".join(re.escape(t) for t in self.sorted_terms) + ")"
        return re.compile(f"{protected_pattern}|{terms_pattern}", re.MULTILINE)

    def process_content(self, content: str, file_path: Path) -> str:
        def replace_func(match: re.Match) -> str:
            g1: Optional[str] = match.group(1)
            g2: Optional[str] = match.group(2)
            if g1: return g1
            if g2:
                term: str = g2
                target_file_key: str = self.mapping[term]
                rel_source: str = get_relative_path(file_path, DOCS_DIR)
                if rel_source == target_file_key: return term
                target_abs: Path = DOCS_DIR / target_file_key
                link_url: str = get_relative_path(target_abs, file_path.parent)
                return f"[{term}]({link_url})"
            return str(match.group(0))
        return self.pattern.sub(replace_func, content)
