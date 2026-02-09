# 🌸 Furuyoni Guide

> **桜降る代に決闘を** 包括的ガイド  
> _A comprehensive guide to Sakura Arms (Furuyoni)_

[![Live Demo](https://img.shields.io/badge/🎴_Live_Demo-kafka2306.github.io/furuyoni-ff69b4?style=for-the-badge)](https://kafka2306.github.io/furuyoni/)
[![Website](https://img.shields.io/website?up_message=online&up_color=success&down_message=offline&down_color=critical&url=https%3A%2F%2Fkafka2306.github.io%2Ffuruyoni%2F&style=for-the-badge&logo=github)](https://kafka2306.github.io/furuyoni/)

## 🔗 [**サイトにアクセス (Open Website)**](https://kafka2306.github.io/furuyoni/)

---

## ✨ Overview

**Furuyoni Guide** は、対戦型カードゲーム「桜降る代に決闘を」の攻略情報を集約したドキュメントサイトです。MkDocsを使用し、初心者から上級者まで活用できるコンテンツを高速かつ美しく提供します。

---

## 📖 Features

- **メガミ一覧**: 全16柱の能力、戦術、カードギャラリー
- **基本ルール**: 初心者向けの用語解説とゲームの流れ
- **ペア攻略**: 厳選された2柱の組み合わせ解説
- **全文検索**: 日本語対応の強力な検索機能
- **レスポンシブ**: モバイル・PC両対応のモダンなUI

---

## 🚀 Development

このプロジェクトは MkDocs と Material テーマを使用して構築されています。

### ローカル環境での起動

```bash
# uv を使用して依存関係のインストールとサーバー起動
task serve
```

ブラウザで `http://localhost:8080` を開きます。

### ビルド

```bash
task build
```

出力先は `site/` ディレクトリです。

---

## 📂 Project Structure

```
furuyoni/
├── docs/                # Markdownソースファイル
├── mkdocs.yml           # MkDocs設定
├── Taskfile.yml         # 開発タスク定義
├── pyproject.toml       # Python依存関係
└── archive/             # 旧HTMLアプリのソース（参照用）
```

---

## 🤝 Acknowledgments

- **BakaFire Party** - 桜降る代に決闘を 公式 (https://main-bakafire.ssl-lolipop.jp/furuyoni/)
- カード画像およびメガミ画像の著作権は BakaFire Party に帰属します。

---

<div align="center">
Made with 🌸 by [kafka2306](https://github.com/kafka2306)
</div>
