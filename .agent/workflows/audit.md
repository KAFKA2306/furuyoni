---
description: 構造および用語の一貫性監査
---

# /audit — 一貫性監査

全ドキュメントを横断的にスキャンし、用語・フォーマット・構造の不統一を検出・修正する。

## 手順

1. `.agent/skills/furuyoni_master/SKILL.md` の **Inspector** と **Navigator** ペルソナを適用する。

// turbo
2. `uv run scripts/maintain.py check-links` を実行し、用語リンクの不足やリンク切れを検出する。

3. 全メガミページ（`docs/megami/*.md`）のセクション構造とカード記述フォーマットが統一されているか検証する。

4. ページ間の相互リンク（おすすめの組み合わせ等）が双方向かつ正確か検証する。

5. 検出された不整合を `notify_user` で報告し、承認後に `replace_file_content` 等で一括修正を適用する。

6. 完了後、`uv run mkdocs build --strict` で整合性を最終確認する。
