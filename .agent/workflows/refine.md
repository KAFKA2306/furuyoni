---
description: 構造・内容・戦略・整合性の包括的・破壊的リファイン
---

# /refine — 包括的マスターワークフロー

`furuyoni_master` スキルの全ペルソナ（Inspector, Navigator, Hajime, Kenshin, Ruri, Sensei, Meijin）を統合し、ドキュメントの品質と整合性を極限まで高める。

## 手順

1. **多角的監査 (Multi-Pass Audit)**
    - `.agent/skills/furuyoni_master/SKILL.md` を読み込み、全7ペルソナを適用して対象ファイルを批評する。
    - 指摘事項を統合し、具体的かつ最小限の修正案（diff形式）を生成する。

2. **自動メンテナンス (Auto-Fix)**
    // turbo
    - `npx ts-node src/main.ts fix` を実行し、リンク切れ修正、カード名同期、アセット更新、アンカー付与を一括適用する。

3. **構造整合性検証 (Structural Audit)**
    // turbo
    - `npx ts-node src/main.ts audit` を実行し、ヘッダー構造、ナビゲーション、リンクの最終検証を行う。

4. **ビルド検証 (Build Verification)**
    // turbo
    - `uv run mkdocs build --strict` でサイト全体のビルドが正常であることを確認する。

5. **適用と報告**
    - 全修正内容を `notify_user` で提示し、承認後に確定させる。
