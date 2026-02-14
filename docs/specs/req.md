# 桜降る代に決闘を - 要求仕様書

## ゲーム概要

桜降る代に決闘を（ふるよに）は、2人のプレイヤーが互いの[ライフ](../mechanics/index.md)を0にすることを目指す対戦型カードゲーム。各プレイヤーは「メガミ」と呼ばれるキャラクターを2柱選択し、それぞれのカードを組み合わせてデッキを構築する。

[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## 基本ルール

### 勝利条件
- 相手プレイヤーの[ライフ](../mechanics/index.md)を0にする
- 何らかの効果によって敗北条件を満たした場合、相手が勝利

### ゲームの準備

#### [桜花結晶](../mechanics/glossary.md)の配置
- [間合](../mechanics/index.md): 10個
- [オーラ](../mechanics/index.md): 各プレイヤー3個
- [ライフ](../mechanics/index.md): 各プレイヤー8個

#### デッキ構築
- メガミ選択: 各プレイヤーは2柱のメガミを選択
- [通常札](../mechanics/index.md): 7枚（山札に配置）
- [切札](../mechanics/index.md): 3枚（[切札](../mechanics/index.md)エリアに裏向きで配置）

#### 初期状態
- 初期手札: 山札から3枚ドロー（入れ替え可能）
- [集中力](../mechanics/index.md): 先攻0、後攻1

### ターン構造

#### [開始フェイズ](../mechanics/flow.md)
- [集中力](../mechanics/index.md)を増やす
- [再構成](../mechanics/flow.md)（山札シャッフル、[ライフ](../mechanics/index.md)1ダメージの可能性）
- カードドロー

#### [メインフェイズ](../mechanics/flow.md)
- 手札からカードを使用
- [基本動作](../mechanics/glossary.md)の実行

#### [終了フェイズ](../mechanics/flow.md)
- ターン終了処理

### [基本動作](../mechanics/glossary.md)

| 動作 | 効果 |
|[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }|[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }|
| [前進](../mechanics/index.md)/[後退](../mechanics/index.md) | [間合](../mechanics/index.md)の[桜花結晶](../mechanics/index.md)を移動し、相手との距離を調整 |
| [宿し](../mechanics/index.md) | [オーラ](../mechanics/index.md)から[フレア](../mechanics/index.md)を得る |
| 離脱 | [ダスト](../mechanics/index.md)から[フレア](../mechanics/index.md)を得る |
| [纏い](../mechanics/index.md) | 山札からカードをドロー |

### カード種別

#### [通常札](../mechanics/glossary.md)
- 攻撃、防御、移動などの基本的な行動
- 山札から引いて使用

#### [切札](../mechanics/glossary.md)
- 強力な効果を持つカード
- [フレア](../mechanics/index.md)（[集中力](../mechanics/index.md)などを消費して得られるコスト）が必要
- 未使用時は裏向き、使用後は表向き

[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## メガミ仕様

### 基本メガミ（16柱）

| ID | メガミ名 | 特徴 |
|[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }-|[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }-|[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }|
| 01 | [ユリナ](../megami/index.md) | 素直な殴り合い性能、大型[切札](../mechanics/index.md)による高打点 |
| 02 | [サイネ](../megami/index.md) | 中距離攻撃、[八相](../mechanics/index.md)による条件付き火力上昇 |
| 03 | [ヒミカ](../megami/index.md) | 遠距離攻撃、[連火](../mechanics/index.md)による連続攻撃 |
| 04 | [トコヨ](../megami/index.md) | 対応（カウンター）、[境地](../mechanics/index.md)による安定性 |
| 05 | [オボロ](../megami/index.md) | [設置](../mechanics/index.md)札によるコンボ、近距離ビートダウン |
| 06 | [ユキヒ](../megami/index.md) | 傘の[開閉](../mechanics/index.md)による得意[間合](../mechanics/index.md)変化、クロック削り |
| 07 | [シンラ](../megami/index.md) | [計略](../mechanics/index.md)による相手ギミック破壊、レンジロック対抗 |
| 08 | [ハガネ](../megami/index.md) | 超火力[切札](../mechanics/index.md)、一撃必殺 |
| 09 | [チカゲ](../megami/index.md) | [毒](../megami/index.md)による持久戦、リソース削り |
| 10 | [クルル](../megami/index.md) | [機巧](../mechanics/index.md)、絡繰、[ダスト](../mechanics/index.md)発生で強化、[切札](../mechanics/index.md)複製 |
| 11 | [サリヤ](../megami/index.md) | [騎動](../mechanics/index.md)、マシン、4フォルム変身、追加[基本動作](../mechanics/glossary.md) |
| 12 | [ライラ](../megami/index.md) | 風雷、爪、[帯電](../mechanics/index.md)解除、高速移動、高攻撃力 |
| 13 | [ウツロ](../megami/index.md) | [灰塵](../mechanics/index.md)、鎌、[ダスト](../mechanics/index.md)12個で強化、[ライフ](../mechanics/index.md)直接削り |
| 14 | [ホノカ](../megami/index.md) | 即興、突霊、ビートダウン、カナヱとのシナジー |
| 15 | [コルヌ](../megami/index.md) | [凍結](../mechanics/index.md)、橇、[オーラ](../mechanics/index.md)[凍結](../mechanics/index.md)、レンジロック、[宿し](../mechanics/index.md)抑制 |
| 16 | [ヤツハ](../megami/index.md) | [鏡映](../mechanics/index.md)、鏡、[鏡映](../mechanics/index.md)数強化、付与札奪取、攻撃反射 |

### メガミデータ構造

```javascript
{
  name: "メガミ名",
  portrait: "images/chara/ico-XX.png",
  cards: [
    "images/card/cards/na_XX_o_n/na_XX_o_n_1.png",
    // ... 7枚のカード画像パス
  ]
}
```

[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## ペア仕様

### ペアの概念
2柱のメガミを組み合わせることで、独自の戦術・シナジーが生まれる。各ペアには固有の戦型名が付けられる。

### 主要ペア一覧

#### 1. 刀薙（[ユリナ](../megami/index.md)/[サイネ](../megami/index.md)）
- 戦型: 高打点ミッドレンジ
- 得意[間合](../mechanics/index.md): 3〜5
- 勝ち筋: 大型[切札](../mechanics/index.md)2枚 + 条件達成（[決死](../mechanics/index.md)・[八相](../mechanics/index.md)）での火力跳ね上がり
- 強み: 条件達成時の異常値打点で相手の受けを破壊
- 弱み: 機動力不足、遠距離レンジロック・超近距離クリンチに弱い

#### 2. 刀扇（[ユリナ](../megami/index.md)/[トコヨ](../megami/index.md)）
- 戦型: バランス型
- 特徴: 攻防バランスが良く、どんな相手にも対応可能
- 強み: 構築調整の柔軟性、初心者〜上級者まで握り続けられる
- 弱み: 「困ったら刀扇」になりやすい

#### 3. 薙扇（[サイネ](../megami/index.md)/[トコヨ](../megami/index.md)）
- 戦型: 万能コントロール
- 特徴: 全ペア屈指の防御力、対応札の多さ
- 強み: 条件（[八相](../mechanics/index.md)・[境地](../mechanics/index.md)）達成時の攻防一致、相手にケアを強制
- 弱み: 条件管理の精度が必要、雑なプレイでは遅いデッキに

#### 4. 銃扇（[ヒミカ](../megami/index.md)/[トコヨ](../megami/index.md)）
- 戦型: [間合](../mechanics/index.md)支配型
- 特徴: 遠距離[連火](../mechanics/index.md) + 近距離対応の両立
- 強み: 相手の対策方針を迷わせる
- 弱み: バランス取り過ぎると決め手が薄い

#### 5. 薙銃（[サイネ](../megami/index.md)/[ヒミカ](../megami/index.md)）
- 戦型: 遠距離レンジロック
- 特徴: [後退](../mechanics/index.md)しながらの攻撃、[連火](../mechanics/index.md)の打点ブースト
- 勝ち筋: 1巡目と中盤以降に2回の攻撃の波を作る
- 強み: 距離と受けの両方にケアを強制
- 弱み: ミスると一気に[ライフ](../mechanics/index.md)が溶ける

#### 6. 刀忍（[ユリナ](../megami/index.md)/[オボロ](../megami/index.md)）
- 戦型: 近距離ビートダウン
- 得意[間合](../mechanics/index.md): 2付近
- 特徴: [設置](../mechanics/index.md)札によるコンボ + 大型[切札](../mechanics/index.md)
- 強み: [オーラ](../mechanics/index.md)を剥がしてからのリーサルが強力
- 弱み: 遠距離レンジロック・[間合](../mechanics/index.md)0クリンチに耐性が低い

#### 7. 忍傘（[オボロ](../megami/index.md)/[ユキヒ](../megami/index.md)）
- 戦型: テクニカルコントロール
- 特徴: [設置](../mechanics/index.md) + 傘の[開閉](../mechanics/index.md)による得意[間合](../mechanics/index.md)変化
- 勝ち筋: クロック的に削りながら終盤リーサル
- 強み: 特定対面（レンジロック相手）に刺さる、回り始めると止まらない
- 弱み: ループが止まる条件（大被弾・[後退](../mechanics/index.md)不能）で破綻

#### 8. 薙書（[サイネ](../megami/index.md)/[シンラ](../megami/index.md)）
- 戦型: ギミック破壊型
- 特徴: 相手のデッキギミック破壊、悠長なプラン否定
- 強み: デッキタイプの射程が広い、対面適応力が高い
- 弱み: 高い知識が必要

#### 9. 銃鎚（[ヒミカ](../megami/index.md)/[ハガネ](../megami/index.md)）
- 戦型: 超重量級ビートダウン
- 特徴: 遠距離攻撃で引きつけ、超火力[切札](../mechanics/index.md)で決着
- 強み: 対応不能な超打点、決まった時の爽快感
- 弱み: コンボパーツを揃えるまでのリソース管理が厳しい

#### 10. 扇[毒](../mechanics/glossary.md)（[トコヨ](../megami/index.md)/[チカゲ](../megami/index.md)）
- 戦型: 持久戦型
- 特徴: [トコヨ](../megami/index.md)の防御力 + [チカゲ](../megami/index.md)の[毒](../megami/index.md)
- 強み: 相手のプランを[毒](../megami/index.md)でズラし続ける
- 弱み: 決定打が遅い、火力で押し切られる可能性

### ペアデータ構造

```javascript
{
  id: number,
  name: "戦型名",
  characters: ["メガミ1", "メガミ2"],
  description: "戦術概要",
  pros: "強み",
  cons: "弱み"
}
```

[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## カード仕様

### カード画像パス規則

#### [通常札](../mechanics/glossary.md)
```
images/card/cards/na_{メガミID}_o_n/na_{メガミID}_o_n_{カード番号}.png
```

例:
- [ユリナ](../megami/index.md)（ID: 01）のカード1: `images/card/cards/na_01_o_n/na_01_o_n_1.png`
- [サイネ](../megami/index.md)（ID: 02）のカード7: `images/card/cards/na_02_o_n/na_02_o_n_7.png`

#### メガミポートレート
```
images/chara/ico-{メガミID}.png
```

例:
- [ユリナ](../megami/index.md): `images/chara/ico-01.png`
- [トコヨ](../megami/index.md): `images/chara/ico-04.png`

### カード枚数
- 各メガミ: 7枚の[通常札](../mechanics/index.md) + 3枚の[切札](../mechanics/index.md)（データ構造上は[通常札](../mechanics/index.md)7枚のみ表示）

[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## 初心者ストーリー仕様

### ストーリーステップ構造

```javascript
{
  id: number,
  title: "英語タイトル",
  subtitle: "日本語サブタイトル",
  description: "ステップの説明",
  focusPair: number, // 対応するペアID
  lessons: [
    "学習ポイント1",
    "学習ポイント2",
    "学習ポイント3"
  ]
}
```

### ストーリー進行（全8ステップ）

| Step | Title | Focus Pair | 学習テーマ |
|[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }|[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }-|[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }|[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }|
| 1 | Awakening | 刀薙 | 基本性能と王道の決闘 |
| 2 | Balance | 刀扇 | 柔軟な対応と基礎力 |
| 3 | Control | 薙扇 | 鉄壁の防御とカウンター |
| 4 | Distance | 銃扇 | [間合](../mechanics/index.md)管理と遠距離の恐怖 |
| 5 | Storm | 薙銃 | 二度の攻撃の波 |
| 6 | Impact | 刀忍 | 圧倒的な近距離破壊力 |
| 7 | Strategy | 忍傘 | 変幻自在なスタイル |
| 8 | Disruption | 薙書 | 相手のプランの破壊 |

[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## データソース

### 公式サイト
- ベースURL: `https://main-bakafire.ssl-lolipop.jp/furuyoni/na/`
- カード画像: 公式サイトの画像パスを直接参照
- 著作権: BakaFire Party

### コミュニティリソース
- ふるよに Advent Calendar: 2023〜2025年の記事アーカイブ（`docs/info/blogs.md`）
- ペア解説: コミュニティプレイヤーによる詳細な戦術解説

[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## 技術仕様

### フロントエンド構成
- HTML: `index.html`（静的ページ）
- JavaScript: ES6モジュール（`src/main.js`, `src/data.js`, `src/story.js`）
- CSS: Pure CSS（`src/style.css`）
- フォント: Noto Sans JP, Outfit（Google Fonts）

### デザイン要件
- 桜吹雪エフェクト: 動的アニメーション
- グラスモーフィズム: モダンUI
- レスポンシブ対応: モバイル/タブレット/デスクトップ
- ダークモード: 目に優しい配色

### パフォーマンス要件
- Vanilla JSで軽量・高速
- Lazy Loadingで画像最適化
- Intersection Observerでスムーズなスクロールアニメーション

[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## 用語集

| 用語 | 説明 |
|[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }|[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }|
| メガミ | プレイヤーが選択するキャラクター |
| [桜花結晶](../mechanics/index.md) | ゲーム内のリソース単位 |
| [間合](../mechanics/index.md) | プレイヤー間の距離 |
| [オーラ](../mechanics/index.md) | プレイヤーの防御リソース |
| [ライフ](../mechanics/index.md) | プレイヤーの生命力（0で敗北） |
| [フレア](../mechanics/index.md) | [切札](../mechanics/index.md)使用のためのコスト |
| [集中力](../mechanics/index.md) | ターン開始時に増加するリソース |
| [通常札](../mechanics/index.md) | 基本的な行動カード |
| [切札](../mechanics/index.md) | 強力な効果を持つカード |
| 対応 | 相手の行動に対するカウンター |
| [設置](../mechanics/index.md) | 次ターン以降に効果を発揮するカード |
| [連火](../mechanics/index.md) | 連続攻撃を可能にする効果 |
| レンジロック | 特定の[間合](../mechanics/index.md)に固定する戦術 |
| クリンチ | [間合](../mechanics/index.md)0に押し込む戦術 |
| ビートダウン | 攻撃的な戦術 |
| コントロール | 防御的・管理的な戦術 |
| ミッドレンジ | 攻防バランス型の戦術 |

[![---](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png)](../assets/images/card/cards/na_14_o_n/na_14_o_n_7.png){ .glightbox }

## 参考文献

1. 公式ルールブック: https://main-bakafire.ssl-lolipop.jp/furuyoni/
2. ふるよに Advent Calendar 2023-2025
3. コミュニティプレイヤー解説記事（`docs/info/blogs.md`参照）
