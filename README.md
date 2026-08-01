# ふるよに統合ガイド

**公開サイト:** https://kafka2306.github.io/furuyoni/

『桜降る代に決闘を 再演』の現行情報と、『新幕 桜降る代に決闘を』シーズン1〜10の蓄積を、版を混同せずに調べるための非公式資料サイトです。

## このサイトの目的

- 現在遊ばれている「再演」の公式情報へ案内する
- 新幕24柱、旧カード、過去シーズン、コミュニティ記事を保存する
- 現行公式、過去の公式、非公式解説、要確認情報を区別する
- 同名カードや同じメガミでも、版ごとの差を確認できるようにする

厳密な裁定、使用可能カード、大会ルールは、必ず現行の公式案内を優先してください。

## 主な入口

| 調べたいこと | ページ |
| --- | --- |
| どの版・フォーマットを見るべきか | [版・フォーマット統合ガイド](docs/status.md) |
| ルールや戦術を調べる | [ルール・戦術索引](docs/rules.md) |
| メガミを探す | [メガミ一覧](docs/megami/index.md) |
| 現行・旧公式資料を探す | [資料索引](docs/resources-index.md) |
| 世界観・物語を調べる | [物語索引](docs/lore-index.md) |
| 新幕のコミュニティ記事を見る | [コミュニティ資料](docs/resources.md) |
| 新幕カード画像を見る | [カード資料](docs/megami/cards.md) |

## 情報の区分

```text
現行公式
過去の公式
非公式の解説・考察
検証待ち
```

これらは別の情報種別として保存します。同名のカードやメガミを版をまたいで自動統合せず、現行裁定には現行公式ソースだけを優先します。

機械可読な定義は[`ontology/project.yaml`](ontology/project.yaml)にあります。

## ローカル実行

### 必要環境

- Python 3.12以上
- `uv`
- `go-task`
- Node.js / npm（監査スクリプト利用時）

### 起動

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

## 主な構成

```text
furuyoni/
├── docs/
│   ├── history/          # 新幕シーズン資料
│   ├── megami/           # メガミ・カード資料
│   ├── status.md         # 版・フォーマット方針
│   ├── rules.md          # ルール・戦術索引
│   ├── resources-index.md
│   └── lore-index.md
├── src/                  # 監査・保守スクリプト
├── mkdocs.yml
├── Taskfile.yml
└── pyproject.toml
```

## 公式サイト

- 再演公式: https://furuyoni.sekiseiro.com/re/
- 新幕旧公式: https://main-bakafire.ssl-lolipop.jp/furuyoni/

## 著作権・免責

本サイトはBakaFire Partyおよび公式運営とは関係のない非公式ファンメイド資料です。カード画像、キャラクター画像、名称、世界観設定などの権利は各権利者に帰属します。

このリポジトリには現時点でライセンスファイルを設置していません。コード・文章・画像を、明示的な許諾なしに再配布可能とは解釈しないでください。

**README最終監査:** 2026-08-01
