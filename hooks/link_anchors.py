from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

CARD_LINK_RE = re.compile(r"\]\(cards\.md#([^)]+)\)")
EXISTING_CARD_ANCHOR_RE = re.compile(r'<span id="[^"]+"></span>')


def _card_anchors(source: str) -> list[str]:
    anchors: list[str] = []
    for match in CARD_LINK_RE.finditer(source):
        anchor = unquote(match.group(1))
        if anchor not in anchors:
            anchors.append(anchor)
    return anchors


def _inject_megami_anchors(markdown: str, docs_dir: Path) -> str:
    # Existing hand-written card ids can repeat across tabs. Replace them with
    # one generated anchor per linked card at the owning Megami section.
    markdown = EXISTING_CARD_ANCHOR_RE.sub("<span></span>", markdown)

    for source_path in sorted((docs_dir / "megami").glob("[0-9][0-9]_*.md")):
        slug = source_path.stem.split("_", 1)[1]
        anchors = _card_anchors(source_path.read_text(encoding="utf-8"))
        if not anchors:
            continue

        section = re.compile(
            rf"^(## .+?\{{:\s*#{re.escape(slug)}\s*\}}\s*)$",
            re.MULTILINE,
        )
        generated = "\n".join(f"[](){{#{anchor}}}" for anchor in anchors)
        markdown, count = section.subn(
            lambda match: f"{match.group(1)}\n\n{generated}",
            markdown,
            count=1,
        )
        if count != 1:
            raise RuntimeError(
                f"megami/cards.md section not found for {source_path.name}: #{slug}"
            )

    return markdown


def on_page_markdown(markdown, page, config, files):
    src_path = page.file.src_path

    if src_path == "megami/cards.md":
        return _inject_megami_anchors(markdown, Path(config["docs_dir"]))

    # These two links pointed at headings that do not exist in their target
    # documents. Keep the destination useful without inventing a new heading.
    if src_path == "index.md":
        return markdown.replace(
            "status.md#まず遊ぶフォーマットを選ぶ",
            "status.md",
        )

    if src_path == "megami/02_saine.md":
        return markdown.replace("](#flare)", "](../rules.md#flare)")

    return markdown
