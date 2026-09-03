https://kafka2306.github.io/furuyoni/

# ふるよに統合ガイド

[![Build and deploy Furuyoni guide](https://github.com/KAFKA2306/furuyoni/actions/workflows/site.yml/badge.svg)](https://github.com/KAFKA2306/furuyoni/actions/workflows/site.yml)

**同じカード名でも、版が違えば「今使える情報」は同じとは限らない。**

過去seasonの記事、旧版の公式資料、現在の再演rule、community解説を一つに混ぜると、昔は正しかった裁定を現行ruleとして読んでしまいます。

このsiteは、『桜降る代に決闘を 再演』の現行情報と『新幕 桜降る代に決闘を』Season 1〜10の蓄積を、**版と情報種別を保ったまま調べる非公式統合ガイド**です。

## Vision

ふるよにの情報探しを「検索結果の日付を見て、どの版か自分で推測する作業」から、**まず現行か過去かを判断し、その版に適用できる公式資料・解説へ安全に辿れる体験**へ変えます。

## Design philosophy

- **Version before content.** 同名card / メガミでも版をまたいで自動統合しない。
- **Current official wins for current rulings.** 現行裁定は再演の最新公式情報を優先する。
- **History is preserved, not promoted.** 旧ruleや旧season資料を消さず、過去情報として明示する。
- **Official and community stay separate.** 公式・過去公式・非公式解説・verification pendingを区別する。
- **Index before duplication.** 同じ資料を複製するより、適切なsourceへ案内する索引を優先する。
- **Unknown scope stays unknown.** どの版に適用するか確認できない情報を現行ruleへ昇格しない。

## Why / 差別化

長く続く対戦gameでは、情報が古いから無価値なのではなく、**どの時点では正しかったかが重要**です。

このguideの差別化は資料数ではありません。再演・新幕・season archive・community contentを同じsiteから探せても、**現行情報と歴史資料を混同しないこと**を中心にします。

MkDocsやontologyは、version boundaryを利用者から隠さないための手段です。

## User journey

```text
知りたいcard / メガミ / ruleを探す
  → version / formatを確認
  → current official / historical official / communityを識別
  → relevant sourceを読む
  → current rulingなら再演公式を最終確認
```

## Main entry points

| 調べたいこと | page |
| --- | --- |
| どの版・formatを見るべきか | [版・フォーマット統合ガイド](docs/status.md) |
| rule / strategy | [ルール・戦術索引](docs/rules.md) |
| メガミ | [メガミ一覧](docs/megami/index.md) |
| current / old official source | [資料索引](docs/resources-index.md) |
| lore / story | [物語索引](docs/lore-index.md) |
| 新幕community article | [コミュニティ資料](docs/resources.md) |
| 新幕card image | [カード資料](docs/megami/cards.md) |

## Information states

```text
現行公式
過去の公式
非公式の解説・考察
検証待ち
```

これらは別情報種別です。同じcard名をversion跨ぎで一つのruleへ潰しません。

Machine-readable definition: [`ontology/project.yaml`](ontology/project.yaml)

## What this guide preserves

- 再演の現行公式情報への入口
- 新幕24柱の資料
- 旧card / past season archive
- official resource index
- community explanation index
- lore / world-building index
- version / format policy

厳密な裁定・legal card・tournament ruleは必ず現行公式を優先してください。

## Quick start

Requirements:

- Python 3.12+
- `uv`
- `go-task`
- Node.js / npm for audit scripts

```bash
git clone https://github.com/KAFKA2306/furuyoni.git
cd furuyoni
uv sync
task dev
```

Open:

```text
http://localhost:8080
```

Validation:

```bash
task build
task check
```

## Repository map

```text
docs/
  history/          Shinmaku season archive
  megami/           Megami / card resources
  status.md         version / format policy
  rules.md          rules / strategy index
  resources-index.md
  lore-index.md
src/                audit / maintenance scripts
ontology/project.yaml
mkdocs.yml
Taskfile.yml
pyproject.toml
```

## Official sources

- 再演公式: https://furuyoni.sekiseiro.com/re/
- 新幕旧公式: https://main-bakafire.ssl-lolipop.jp/furuyoni/

## Done

成功指標は過去資料をすべて現行形式へ統合することではありません。

**利用者が調べたい情報について「これは現行公式・過去公式・非公式・未確認のどれか」を見分け、現在遊ぶために使ってよいsourceへ到達できること**をDoneとします。

## Rights / disclaimer

本siteはBakaFire Partyおよび公式運営とは関係のない非公式fan-made resourceです。card画像、character画像、名称、world setting等の権利は各権利者に帰属します。

現時点でrepository license fileはありません。code / text / imageを明示許諾なしに再配布可能とは解釈しないでください。
