---
description: 構造・内容・戦略の包括的リファイン（監査・レビュー・深化の統合）
---

# /refine — 包括的リファイン

`furuyoni_master` の全ペルソナ（7種）をフル活用し、構造・内容・戦略の全てを一挙に最適化する。

## 手順

1. `.agent/skills/furuyoni_master/SKILL.md` を読み込む。

2. 以下の3段階で全自動リファインを実施：
    - **構造監査 (Inspector/Navigator)**: セクション順序、リンク整合性、ナビゲーションの検証。
    - **内容レビュー (Hajime/Kenshin/Ruri)**: 読みやすさ、戦略的妥当性、ルール正確性の検証。
    - **戦略深化 (Sensei/Meijin)**: 実用的な具体性と Season 10 メタへの適合を強化。

3. 全指摘を統合し、優先度順に並べた包括的な diffパッチを生成する。

// turbo
4. `notify_user` で提案を提示し、承認後に修正を一括適用する。

5. `uv run mkdocs build --strict` で最終的な整合性を検証する。
