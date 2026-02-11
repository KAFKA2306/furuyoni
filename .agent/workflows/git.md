---
description: Git操作（ステータス確認、追加、コミット、プッシュ）
---

# /git — Git操作

一連のGit操作（status, add, commit, push）を順番に実行する。

## 手順

// turbo-all

1. 現在の状態を確認する:
   ```bash
   git status
   ```

2. 全ての変更をステージングする:
   ```bash
   git add .
   ```

3. 変更をコミットする（メッセージは状況に応じて調整）:
   ```bash
   git commit -m "chore: update documentation and agent settings"
   ```

4. リモートリポジトリにプッシュする:
   ```bash
   git push
   ```

5. 完了後、`git log -n 1` で最新のコミットを確認して報告する。
