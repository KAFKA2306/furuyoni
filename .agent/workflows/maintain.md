---
description: メンテナンスタスク一括実行
---

# /maintain — メンテナンス一括実行

既存の `scripts/maintain.py` の全サブコマンドを順次実行し、サイト健全性を維持する。

## 手順

// turbo-all

1. リンク切れ検出:
   ```bash
   uv run scripts/maintain.py check-links
   ```

2. 用語リンク自動付与:
   ```bash
   uv run scripts/maintain.py add-links
   ```

3. アセットダウンロード:
   ```bash
   uv run scripts/maintain.py download-assets
   ```

4. ビルド検証:
   ```bash
   uv run mkdocs build --strict
   ```

5. 結果をサマリーとして `notify_user` でユーザーに報告する:
   - リンク切れの有無と件数
   - 新規リンク付与の件数
   - ダウンロードしたアセットの件数
   - ビルド成功/失敗
