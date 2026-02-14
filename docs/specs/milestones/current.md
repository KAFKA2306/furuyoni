# マイルストーン: MkDocs移行計画

> 日付: 2026-02-08  
> 目的: 現行HTMLアプリからMkDocsベースの静的ドキュメントサイトへ移行

[![---](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## 背景と理由

### 現行HTMLの課題
1. View表示の不具合 - コンテンツが見切れる問題が発生
2. AIエージェントによる認識困難 - ブラウザでの視覚的確認に依存
3. 保守性 - カスタムCSS/JSの管理が複雑化
4. 検索機能なし - 大量のドキュメントから情報を探しにくい

### MkDocs採用のメリット
- Markdownネイティブ - 既存の`docs/info/*.md`をそのまま活用
- 全文検索 - プラグインで自動提供
- テーマ（Material） - モダンで美しいUI、レスポンシブ対応
- 目次・ナビ自動生成 - 手動管理不要
- GitHub Pages対応 - 現行と同じホスティング

[![---](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## 移行対象ファイル

### 既存コンテンツ（そのまま移行）
| ファイル | 移行先 | 内容 |
|:[![---](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }|:[![---](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }|:[![---](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }|
| `docs/info/00_overview.md` | `docs/overview.md` | ゲーム概要 |
| `docs/info/01_mechanics.md` | `docs/mechanics.md` | ルール・メカニクス |
| `docs/info/02_megami_roster.md` | `docs/megami/index.md` | メガミ一覧 |
| `docs/info/03_game_flow.md` | `docs/mechanics/flow.md` | ゲームの流れ |
| `docs/info/04_beginner_curriculum.md` | `docs/beginner/curriculum.md` | 初心者カリキュラム |
| `docs/info/pair.md` | `docs/pairs/index.md` | ペア攻略 |
| `docs/info/blogs.md` | `docs/community/blogs.md` | コミュニティ記事 |

### HTMLから変換が必要
| ファイル | 対応 |
|:[![---](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }|:[![---](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }|
| `docs/info/cards.html` | → Markdown化（画像ギャラリー形式） |
| `docs/info/chara.html` | → Markdown化（テーブル形式） |

### 削除対象
- `index.html` - MkDocsのビルド結果で置換
- `main.js`, `story.js`, `megami.js`, `mechanics.js` - MkDocsで不要
- `style.css` - Material テーマで代替

[![---](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## 新しいディレクトリ構造

```
furuyoni/
├── docs/                      # MkDocsソース
│   ├── index.md               # トップページ
│   ├── overview.md            # 概要
│   ├── mechanics/
│   │   ├── index.md           # ルール概要
│   │   └── flow.md            # ゲームの流れ
│   ├── megami/
│   │   ├── index.md           # メガミ一覧
│   │   └── cards.md           # カード画像ギャラリー
│   ├── pairs/
│   │   ├── index.md           # ペア一覧
│   │   └── details/           # 各ペアの詳細ページ（将来拡張）
│   ├── beginner/
│   │   └── curriculum.md      # 初心者カリキュラム
│   ├── community/
│   │   └── blogs.md           # コミュニティ記事
│   └── assets/
│       └── images/            # ローカル画像（必要に応じて）
├── mkdocs.yml                 # MkDocs設定
├── data.js                    # 参照用（移行後削除可）
└── site/                      # ビルド出力（GitHub Pagesへデプロイ）
```

[![---](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## MkDocs設定 (`mkdocs.yml`)

```yaml
site_name: ふるよに ガイド
site_url: https://kafka.github.io/furuyoni/
site_description: 桜降る代に決闘を - 初心者向けペアガイド＆攻略情報

theme:
  name: material
  language: ja
  palette:
    - scheme: slate
      primary: pink
      accent: cyan
      toggle:
        icon: material/brightness-4
        name: ライトモードに切替
    - scheme: default
      primary: pink
      accent: cyan
      toggle:
        icon: material/brightness-7
        name: ダークモードに切替
  features:
    - navigation.sections
    - navigation.expand
    - navigation.top
    - search.highlight
    - content.tabs.link
  font:
    text: Noto Sans JP
    code: Roboto Mono

nav:
  - ホーム: index.md
  - 概要: overview.md
  - ルール:
    - 基本ルール: mechanics/index.md
    - ゲームの流れ: mechanics/flow.md
  - メガミ:
    - 一覧: megami/index.md
    - カード: megami/cards.md
  - ペア攻略:
    - ペア一覧: pairs/index.md
  - 初心者向け:
    - 入門カリキュラム: beginner/curriculum.md
  - コミュニティ:
    - ブログ記事: community/blogs.md

plugins:
  - search:
      lang: ja
  - glightbox  # 画像ギャラリー用

markdown_extensions:
  - tables
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - attr_list
  - md_in_html

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/kafka/furuyoni
```

[![---](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## 実装ステップ

### Phase 1: 環境構築 (30分)
- [x] `pip install mkdocs-material mkdocs-glightbox`
- [x] `mkdocs.yml` 作成
- [x] ディレクトリ構造の整理

### Phase 2: コンテンツ移行 (60分)
- [x] 既存Markdownファイルの移動・リネーム
- [x] `cards.html` → `megami/cards.md` 変換
- [x] `chara.html` → `megami/index.md` 統合
- [x] 画像パスの確認と修正

### Phase 3: トップページ作成 (30分)
- [x] `docs/index.md` 作成（ヒーローセクション＋クイックリンク）
- [x] Material テーマの機能活用（アイコン、グリッド）

### Phase 4: ビルド＆デプロイ (30分)
- [x] `mkdocs build` で `site/` 生成
- [x] GitHub Actions ワークフロー更新
- [x] GitHub Pages へデプロイ確認

### Phase 5: クリーンアップ (15分)
- [x] 旧HTML/JS/CSSファイル削除
- [x] README更新
- [x] `.gitignore` に `site/` 追加

[![---](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## 旧資産の保存

インタラクティブなJSロジック（将来再利用の可能性）：
- `data.js` → `archive/data.js`
- `story.js` → `archive/story.js`
- `style.css` → `archive/style.css`

[![---](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## 検証項目

- [x] 全ページがローカルで正しく表示される (`mkdocs serve`)
- [x] 画像が正しく読み込まれる（外部URL / ローカル）
- [x] 検索機能が日本語で動作する
- [x] モバイル表示が崩れない
- [x] GitHub Pages でデプロイ後アクセス可能

[![---](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## リスクと対策

| リスク | 対策 |
|:[![---](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }|:[![---](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }|
| 画像URLが壊れる | 移行前に全画像URLを検証 |
| 検索が日本語非対応 | `lunr[ja]` プラグイン追加 |
| カスタムデザイン喪失 | Material テーマ + `extra.css` で補完 |

[![---](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## 完了条件

1. `https://kafka.github.io/furuyoni/` でMkDocsサイトが表示される
2. 全てのドキュメントページがナビゲーションからアクセス可能
3. 検索で「[ユリナ](../../megami/index.md)」「刀薙」等の日本語検索が機能する
4. カード画像が正しく表示される
