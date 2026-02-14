---
description: 5ペルソナによる多角的批評と戦略強化
---

# /critique — 多角的コンテンツ批評

`furuyoni_master` の主要5ペルソナ（Hajime/Kenshin/Ruri/Sensei/Meijin）を全適用し、コンテンツを徹底的に批評する。

## 手順

1. `.agent/skills/furuyoni_master/SKILL.md` を読み込む。

2. 全5ペルソナで順次レビューを実行し、初心者視点から上級者メタまでの広範な指摘を収集する。

3. 各視点からの指摘を統合し、矛盾を解消した上で、具体的な改善案を diff 形式で生成する。

// turbo
4. `notify_user` で提案を提示し、承認後に一括適用。
