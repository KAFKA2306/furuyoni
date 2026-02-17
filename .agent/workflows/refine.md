---
description: 構造・内容・戦略・整合性の包括的・破壊的リファイン（厳格モード）からのGit操作（ステータス確認、追加、コミット、プッシュ）
---

# /refine — 包括的マスターワークフロー（STRICT）

`furuyoni_master` スキルの全ペルソナ（Inspector, Navigator, Hajime, Kenshin, Ruri, Sensei, Meijin）を統合し、ドキュメントの品質と整合性を極限まで高める。

**厳格ルール**: 画像重複、リンク切れ、構造エラーは**一切許容しない**。すべての検証で失敗した場合、修正するまでビルドを通さない。


変更のリポジトリ反映を一括で行う。

## 手順

1. **多角的監査 (Multi-Pass Audit)**
    - `.agent/skills/furuyoni_master/SKILL.md` の新チェックリストを読み込む。
    - 全7ペルソナを適用し、**「ペルソナ別監査レポート」**を作成してから修正案を生成する。

2. **自動メンテナンス (Auto-Fix)**
    // turbo
    - `npx ts-node src/main.ts fix` を実行。
    - 指標：リンク修正、カード名同期、アセット更新、アンカー付与（`{: #Name }`形式）。

3. **構造整合性検証 (Structural Audit) — STRICT**
    // turbo
    - `npx ts-node src/main.ts audit` を実行し、以下を**強制検証**:
        - H1はファイルに1つのみ。ヘッダーのレベルスキップ禁止。
        - **画像の重複：同一画像は3回以上出現で問答無用でエラー。**
        - `index.md` の `hero-section`, `dashboard-grid` クラス。
    - **エラーが1つでもあればステージングせず、修正に戻る。**

4. **ビルド検証 (Build Verification) — STRICT**
    // turbo
    - `uv run mkdocs build --strict` でビルド。
    - **Warning（警告）を1つも残さない。すべて解消する。**

5. **CI/CD 同期と検証**
    // turbo
    - `gh run watch` を実行し、直近のビルドが完了するまで待機する。
    - `gh run list --limit 1` でステータスが `completed` かつ `success` であることを確認。

6. **適用と完了**
    - `git add .`
    - `git commit -m "docs: <内容> (Audit Passed, S10 Validated)"`
    - `git push`

7. **最終視覚監査 (Visual Audit) — Browser Subagent**
    - `browser_subagent` を起動。
    - `mkdocs.yml` の `site_url` ( https://kafka2306.github.io/furuyoni/ ) にアクセス。
    - **重点チェック項目**:
        - [ ] **Console/Network**: コンソールにエラー（404, JSエラー）が出ていないか？
        - [ ] **Asset Integrity**: カード画像やアイコンが Alt テキストではなく、正しくレンダリングされているか？
        - [ ] **Functional Audit**: カード名リンク（アンカー）をクリックし、正しい位置にジャンプするか？
        - [ ] **UI Audit**: `hero-section` や `dashboard-grid` のレイアウトが崩れていないか？
        - [ ] **Policy Check**: Role Badge 等が画像ではなくテキストで表示されているか？
    - 各チェック項目のスクリーンショットを撮影し、問題があれば `notify_user` で報告する。

8. `git log -n 1` で最終結果を報告。