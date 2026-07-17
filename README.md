# ふるよに 統合ガイド

『桜降る代に決闘を 再演』の現行公式情報と、『新幕 桜降る代に決闘を』シーズン1〜10の蓄積を、対象版を混同せずに参照するための非公式サイトです。

- 公開サイト: https://kafka2306.github.io/furuyoni/
- 再演公式サイト: https://furuyoni.sekiseiro.com/re/
- 新幕旧公式サイト: https://main-bakafire.ssl-lolipop.jp/furuyoni/

## 方針

このリポジトリは、旧資料を捨てて再演だけへ置き換えるものではありません。

- 再演起源戦・完全戦・古典戦の公式情報へ案内する
- 新幕24柱、旧カード、シーズン1〜10、コミュニティ記事をアーカイブとして保存する
- 現行公式、旧公式、非公式解説、検証待ちを区分する
- 同名カードや同じメガミでも、再演と新幕の差を確認して利用する
- 厳密な裁定、使用可能カード、大会情報は公式案内を優先する

詳細はサイト内の「版・フォーマット統合ガイド」を参照してください。

## 主な入口

| 目的 | ページ |
| --- | --- |
| 版・フォーマットを選ぶ | `docs/status.md` |
| ルール・戦術を調べる | `docs/rules.md` |
| メガミを探す | `docs/megami/index.md` |
| 現行・旧公式資料を探す | `docs/resources-index.md` |
| 世界観・物語を調べる | `docs/lore-index.md` |
| 新幕コミュニティ記事を見る | `docs/resources.md` |
| 新幕カード画像を見る | `docs/megami/cards.md` |

## ローカル実行

### 必要環境

- Python 3.12以上
- `uv`
- `go-task`（Taskfileを利用する場合）
- Node.js / npm（監査スクリプトを利用する場合）

### 開発サーバー

```bash
git clone https://github.com/KAFKA2306/furuyoni.git
cd furuyoni
uv sync
task dev
```

`http://localhost:8080`で確認できます。

### 検証

```bash
task build   # MkDocs strict build
task check   # TypeScript監査 + MkDocs strict build
```

## ディレクトリ

```text
furuyoni/
├── docs/
│   ├── history/          # 新幕シーズン資料
│   ├── megami/           # 新幕メガミ・カード資料
│   ├── status.md         # 版・フォーマット方針
│   ├── rules.md          # 統合ルール・戦術索引
│   ├── resources-index.md
│   └── lore-index.md
├── src/                  # 監査・保守スクリプト
├── mkdocs.yml
├── Taskfile.yml
└── pyproject.toml
```

## 著作権・免責

本サイトは非公式のファンメイド資料です。BakaFire Partyおよび公式運営によるものではありません。

カード画像、キャラクター画像、名称、世界観設定などの権利は、それぞれの権利者に帰属します。公式素材の利用条件と公式ガイドラインを優先してください。

このリポジトリには、現時点でライセンスファイルを設置していません。リポジトリ内のコード・文章・画像を、明示的な許諾なしに再配布可能とは解釈しないでください。

**最終方針更新:** 2026年7月17日
