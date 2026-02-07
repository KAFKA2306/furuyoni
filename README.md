# 🌸 Furuyoni Pair Guide

> **桜降る代に決闘を** 初心者向けペアガイド  
> _A beginner-friendly guide to mastering character pairs in Sakura Arms_

[![Live Demo](https://img.shields.io/badge/🎴_Live_Demo-kafka2306.github.io/furuyoni-ff69b4?style=for-the-badge)](https://kafka2306.github.io/furuyoni/)

---

## ✨ Overview

**Furuyoni Pair Guide** は、対戦型カードゲーム「桜降る代に決闘を」の初心者向けペア紹介サイトです。各メガミの組み合わせによる戦術・勝ち筋を、視覚的かつインタラクティブに学べます。

An immersive, interactive web experience designed to help beginners understand character pair synergies, strategies, and win conditions in _Sakura Arms_ (Furuyoni).

---

## 🎯 Features

### 🎴 **Pair Guide**
- **主要ペア一覧**: 初心者におすすめの組み合わせを厳選
- **戦術解説**: 各ペアの強み・弱み・勝ち筋を詳細に紹介
- **カード閲覧**: 公式サイトの画像を使用し、各メガミのカードを確認可能
- **インタラクティブUI**: ホバーエフェクト・モーダル表示で直感的に操作

### 📖 **Beginner Story**
- **段階的学習**: ミコトの成長物語に沿って、基礎から応用まで学習
- **実戦的レッスン**: 各ステップで具体的な戦術ポイントを提示
- **Focus Pair連携**: ストーリーから直接ペア詳細へジャンプ可能

### 🎨 **Premium Design**
- **桜吹雪エフェクト**: 和風の雰囲気を演出する動的アニメーション
- **グラスモーフィズム**: モダンで洗練されたUI
- **レスポンシブ対応**: モバイル・タブレット・デスクトップ全対応
- **ダークモード**: 目に優しい配色設計

---

## 🚀 Quick Start

### **ローカル環境で実行**

```bash
task serve
```

ブラウザで `http://localhost:8080` を開く

### **デプロイ済みサイト**

👉 **[https://kafka2306.github.io/furuyoni/](https://kafka2306.github.io/furuyoni/)**

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Core** | Vanilla JavaScript (ES6 Modules) |
| **Styling** | Pure CSS (Glassmorphism, Animations) |
| **Fonts** | Noto Sans JP, Outfit (Google Fonts) |
| **Assets** | Official Furuyoni card images |
| **Build** | Static HTML (No bundler) |
| **Deploy** | GitHub Pages |

---

## 📂 Project Structure

```
furuyoni/
├── index.html              # メインHTML
├── main.js                 # アプリケーションロジック
├── data.js                 # ペア・カードデータ
├── mechanics.js            # ルール・メカニクスデータ
├── megami.js               # メガミ一覧データ
├── story.js                # 初心者ストーリーデータ
├── style.css               # スタイル定義
├── docs/                  # 追加ドキュメント
├── Taskfile.yml           # タスク定義
└── README.md              # このファイル
```

---

## 🎨 Design Philosophy

### **視覚的インパクト**
- 桜吹雪の動的アニメーションで和風の世界観を表現
- グラデーション・シャドウ・ホバーエフェクトで premium な体験を提供

### **初心者フレンドリー**
- 複雑な戦術を「一言で伝わる粒度」に凝縮
- ストーリー形式で段階的に学習できる構成

### **パフォーマンス**
- Vanilla JS で軽量・高速
- Lazy Loading で画像読み込みを最適化
- Intersection Observer でスムーズなスクロールアニメーション

---

## 📸 Screenshots

### Pair Guide View
![Pair Grid](https://via.placeholder.com/800x400/1a1a2e/ff69b4?text=Pair+Guide+Grid)

### Modal Detail
![Pair Detail](https://via.placeholder.com/800x400/16213e/4ecca3?text=Pair+Detail+Modal)

### Beginner Story
![Story Timeline](https://via.placeholder.com/800x400/0f3460/f39c12?text=Story+Timeline)

---

## 🤝 Contributing

このプロジェクトは個人開発ですが、改善提案・バグ報告は歓迎します。

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

このプロジェクトのコードは MIT License です。  
カード画像の著作権は **BakaFire Party** に帰属します。

---

## 🙏 Acknowledgments

- **BakaFire Party** - 桜降る代に決闘を 公式
- **Google Fonts** - Noto Sans JP, Outfit
- **Community** - ふるよにプレイヤーコミュニティ

---

<div align="center">

**Made with 🌸 by [kafka2306](https://github.com/kafka2306)**

[🎴 Visit Live Site](https://kafka2306.github.io/furuyoni/) • [📖 Documentation](./docs/) • [🐛 Report Bug](https://github.com/kafka2306/furuyoni/issues)

</div>
