---
description: 構造・SEO・リンク・アセットの自動最適化
---

# /optimize — システム最適化

サイト全体の健全性を維持するためのメンテナンス処理を一括実行する。

## 手順

// turbo-all

1. `uv run scripts/maintain.py check-links` でリンク切れを検証。
2. `uv run scripts/maintain.py add-links` で用語集へのリンクを自動付与。
3. `uv run scripts/maintain.py download-assets` で画像アセットを同期。
4. `uv run mkdocs build --strict` でビルドの正常性を検証。

5. 実行結果のサマリーを `notify_user` で報告する。
