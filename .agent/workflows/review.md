---
description: 3ペルソナによる多角的なコンテンツレビュー
---

# /review — コンテンツレビュー

`furuyoni_master` の Hajime/Kenshin/Ruri ペルソナを適用し、コンテンツの品質を監査する。

## 手順

1. `.agent/skills/furuyoni_master/SKILL.md` を読み込み、対象ファイルを特定する。

2. 以下のペルソナで個別に監査を実施する：
    - **Hajime**: 初級者の視点での読みやすさと理解度。
    - **Kenshin**: 戦術的な妥当性と実用性。
    - **Ruri**: ルールおよび用語の正確性（Season 10準拠）。

3. 指摘事項を統合し、具体的な改善案を diff 形式で作成する。

// turbo
4. `notify_user` で提案を提示し、承認後に修正を直接適用する。

5. `uv run mkdocs build --strict` でサイトの正常性を確認する。
