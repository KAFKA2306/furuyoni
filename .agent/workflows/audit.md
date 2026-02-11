---
description: 全ドキュメント横断の一貫性監査
---

# /audit — 一貫性監査

全ドキュメントを横断的にスキャンし、用語・フォーマット・構造の不統一を検出・修正する。

## 手順

1. `.agent/skills/furuyoni_auditor/SKILL.md` を読み込む。

// turbo
2. `config.yaml` の `term_mapping` を読み込み、全 `.md` ファイルで未リンクの用語を検出する。
   ```bash
   uv run scripts/maintain.py check-links
   ```

3. 全メガミページ（`docs/megami/01_yurina.md` 〜 `16_yatsuha.md`）のセクション構造を比較する:
   - 必須セクション: `本質的な解説`, `キーワード能力`, `通常札の一覧`, `切り札の一覧`, `戦術の核心`, `おすすめの組み合わせ`
   - セクション順序の統一性
   - カード記述フォーマットの統一性（画像パス形式、説明文の長さ）

4. **Inspector ペルソナ** で以下を検証:
   - 全ページで同一タームが同一表記か（揺れ検出）
   - リンク先が正しいか（内部リンクのパス整合性）
   - 画像パスがローカル/外部で統一されているか

5. **Navigator ペルソナ** で以下を検証:
   - 全ページから到達可能か（孤立ページの検出）
   - 「おすすめの組み合わせ」の相互リンクが双方向か
   - `mkdocs.yml` の `nav` に全ページが登録されているか

6. 不統一項目をリスト化し、`notify_user` でユーザーに提示する。

7. 承認後:
// turbo
   - `uv run scripts/maintain.py add-links` で用語リンクを自動付与
   - 個別修正は `replace_file_content` で適用
