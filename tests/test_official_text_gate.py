from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.official_text_gate import audit_card_file, audit_file, validate_card_marker, validate_marker


class OfficialTextGateTests(unittest.TestCase):
    def test_source_quote_is_required_and_verified(self) -> None:
        manifest = {
            "sources": {
                "rules": {"format": "pdf", "refs": ["4-"]},
            },
        }
        marker = __import__("re").search(
            r"<!--\s*official-source:\s*([\w-]+)#([^|\s]+)\s*\|\s*quote:\s*(.*?)\s*-->",
            "<!-- official-source: rules#4-1 | quote: 初期配置 -->",
        )
        self.assertIsNotNone(marker)
        self.assertIsNone(validate_marker(marker, {"rules": "4-1初期配置"}, manifest))
        self.assertIn("quote not found", validate_marker(marker, {"rules": "4-1別の文"}, manifest) or "")

    def test_unmarked_rule_claim_blocks(self) -> None:
        policy = {
            "rule_terms": ["オーラ"],
            "claim_patterns": [r"[0-9０-９]+個"],
        }
        manifest = {"sources": {}}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "claim.md"
            path.write_text("オーラは5個。\n", encoding="utf-8")
            violations = audit_file(path, policy, {}, manifest)
        self.assertEqual(len(violations), 1)
        self.assertIn("no official quote", violations[0].message)

    def test_card_quote_is_required_and_verified(self) -> None:
        manifest = {"sources": {"cardlist": {"format": "pdf_ocr"}}}
        marker = __import__("re").search(
            r"<!--\s*official-card:\s*([\w-]+)#([^|\s]+)\s*\|\s*quote:\s*(.*?)\s*-->",
            "<!-- official-card: cardlist#test-card | quote: 3/2 -->",
        )
        self.assertIsNotNone(marker)
        self.assertIsNone(validate_card_marker(marker, {"cardlist": "3/2"}, manifest))
        self.assertIn("card quote not found", validate_card_marker(marker, {"cardlist": "2/1"}, manifest) or "")

    def test_unmarked_card_effect_blocks(self) -> None:
        policy = {"card_claim_patterns": [r"解説"]}
        manifest = {"sources": {}}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "card.md"
            path.write_text("### [試験札](cards.md#試験札)\n\n* **解説**: 効果説明\n", encoding="utf-8")
            violations = audit_card_file(path, policy, {}, manifest)
        self.assertEqual(len(violations), 1)
        self.assertIn("card effect text", violations[0].message)


if __name__ == "__main__":
    unittest.main()
