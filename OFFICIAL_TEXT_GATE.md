# Official text gate

`scripts/official_text_gate.py` is a fail-closed provenance check for rule-bearing text.

It downloads the BakaFire Party sources listed in `config/official_sources.yaml`, checks their SHA-256 values, extracts searchable text from the rule PDF and FAQ, and scans `docs/` plus the local Furuyoni rule references.

A factual rule claim must carry a marker in the same paragraph:

```markdown
<!-- official-source: comprehensive#4-1 | quote: ＜間合＞に 10 個 -->
間合は10で開始する。
```

Card effect explanations use the card-list marker:

```markdown
<!-- official-card: cardlist#黒き波動 | quote: 3/2 -->
* **ダメージ**: 3/2
```

The quoted fragment must exist in the pinned official source or the OCR corpus generated from the pinned official card list. Missing quotes, unknown references, binary-only sources, OCR misses, and source hash changes block the build. The gate reports violations; it never guesses a replacement or deletes content automatically.

Run it with:

```bash
task official-text-gate
task check
```

`--offline` uses only the local source cache. A source cache is ignored by Git.
