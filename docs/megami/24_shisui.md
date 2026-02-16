# シスイ

<div class="megami-hud" style="display: grid; grid-template-columns: 100px 1fr; gap: 20px; background: rgba(0,0,0,0.05); padding: 20px; border-radius: 10px; border-left: 5px solid #5d4037;">
  <img src="" width="100">
  <div class="hud-content">
    <div style="font-size: 1.5em; font-weight: bold; margin-bottom: 5px;">【鋸】シスイ / Season 10</div>
    <div style="display: flex; gap: 15px; font-size: 0.9em;">
      <span>難易度: ★★★☆☆</span>
      <span>[間合](../rules.md#range): 2-3</span>
      <span>タイプ: ビートダウン</span>
      <span style="color: #d32f2f; font-weight: bold;">S10 Meta: Tier 1 (Aggro)</span>
    </div>
  </div>
</div>

## S10 環境分析
```mermaid
graph LR
    A[アキナ/レンリ弱体化] --> B(中速環境への移行)
    C[裂傷による遅延ダメージ] --> D(バーストリーサルの否定)
    B --> E[シスイのハドマギリ戦術が刺さる]
    D --> E
```

> [!CAUTION]
> **初心者が陥る致命的な罠**
> - **無計画な自傷**: シスイは自ら「裂傷」を負うことで火力を出すが、[ライフ](../rules.md#life)5以下での過度な自傷はセルフリーサルを招く。
> - **ハドマギリの温存しすぎ**: [フレア](../rules.md#flare)2で撃てるこの札は、中盤のダメージレースを優位に進めるために早期使用も選択肢。

## 戦略的タイムライン

### Phase 1: 開幕 (Turn 1-2)
- **目的**: 『徹底抗戦』や『刻み込み』で相手に「裂傷」を植え付ける。
- **推奨挙動**: [前進](../rules.md#advance)を優先し、[間合](../rules.md#range)3をキープ。

### Phase 2: 中盤 (Turn 3-5)
- **目的**: 相手の[オーラ](../rules.md#aura)上限を裂傷で削り、[ライフ](../rules.md#life)への通りを良くする。
- **決戦準備**: 自身の裂傷を『反乱撃』でバフに変換し、高火力のプレッシャーをかける。

### Phase 3: 終盤 (リーサル)
- **目的**: 『ハドマギリ』による裂傷即時発動で、相手の計算を狂わせて落とす。

## [通常札](../rules.md)性能マトリクス

| カード名 | 主な役割 | 特徴 | S10 特記事項 |
| :--- | :--- | :--- | :--- |
| **[![鋸斬り](../assets/images/card/cards/na_24_o_n/na_24_o_n_1.png)](../assets/images/card/cards/na_24_o_n/na_24_o_n_1.png){ .glightbox }** | 主力攻撃 | 2/2 相手に裂傷付与 | 基本性能の塊。 |
| **[![刻み刃](../assets/images/card/cards/na_24_o_n/na_24_o_n_2.png)](../assets/images/card/cards/na_24_o_n/na_24_o_n_2.png){ .glightbox }** | 継続火力 | 1/1 攻撃後、裂傷を深める | [オーラ](../rules.md#aura)を剥がした後に有効。 |
| **[![茨道](../assets/images/card/cards/na_24_o_n/na_24_o_n_3.png)](../assets/images/card/cards/na_24_o_n/na_24_o_n_3.png){ .glightbox }** | 位置調整 | 移動 + 相手に裂傷 | レンジロック対策の要。 |
| **[![反乱撃](../assets/images/card/cards/na_24_o_n/na_24_o_n_4.png)](../assets/images/card/cards/na_24_o_n/na_24_o_n_4.png){ .glightbox }** | 自己強化 | 自身の裂傷を火力に変換 | **リーサルパーツ**。 |
| **[![金屑纏い](../assets/images/card/cards/na_24_o_n/na_24_o_n_5.png)](../assets/images/card/cards/na_24_o_n/na_24_o_n_5.png){ .glightbox }** | リソース | 相手リソース奪取 + 自オーラ回復 | 粘り強く戦うために。 |
| **[![徹底抗戦](../assets/images/card/cards/na_24_o_n/na_24_o_n_6.png)](../assets/images/card/cards/na_24_o_n/na_24_o_n_6.png){ .glightbox }** | 妨害 | 攻撃を裂傷化して与える | 相手の「構築」を狂わせる。 |
| **[![蹂躙](../assets/images/card/cards/na_24_o_n/na_24_o_n_7.png)](../assets/images/card/cards/na_24_o_n/na_24_o_n_7.png){ .glightbox }** | 強襲 | 高い貫通力を持つ全力攻撃。 | 一気にライフを削る。 |

## [切札](../rules.md)：必殺の定義

| 名称 | コスト | 種別 | 解説 |
| :--- | :--- | :--- | :--- |
| **[![ハドマギリ](../assets/images/card/cards/na_24_o_s/na_24_o_s_1.png)](../assets/images/card/cards/na_24_o_s/na_24_o_s_1.png){ .glightbox }** | 2 | 攻撃 | **フィニッシャー**。裂傷ダメージを即座に処理する。 |
| **[![ウバラザキ](../assets/images/card/cards/na_24_o_s/na_24_o_s_2.png)](../assets/images/card/cards/na_24_o_s/na_24_o_s_2.png){ .glightbox }** | 5 | 攻撃 | [フレア](../rules.md#flare)裂傷によるリソース破壊。 |
| **[![アブダグイ](../assets/images/card/cards/na_24_o_s/na_24_o_s_3.png)](../assets/images/card/cards/na_24_o_s/na_24_o_s_3.png){ .glightbox }** | 3 | 対応 | **防御の要**。致命傷を避けるためのクッション。 |
| **[![ヂーガデハド](../assets/images/card/cards/na_24_o_s/na_24_o_s_4.png)](../assets/images/card/cards/na_24_o_s/na_24_o_s_4.png){ .glightbox }** | 4 | 攻撃 | 裂傷の多さに応じて威力が跳ね上がる一撃。 |

## カード個別解説

### N10 鋸斬り
裂傷の起点となる、シスイの基本攻撃。

### N10 刻み刃
連続して裂傷を与えることで、相手の[ライフ](../rules.md#life)を追い詰める。

### N10 茨道
間合を詰めつつ、相手に裂傷のプレッシャーを与える移動札。

### N10 反乱撃
自身が負った裂傷を糧に、破壊的な一撃を放つ。

### N10 金屑纏い
裂傷を負いながらも、自身の[オーラ](../rules.md#aura)を強固に保つ。

### N10 徹底抗戦
相手の攻撃計算を狂わせ、裂傷によるジレンマを強いる。

### N10 蹂躙
相手の防御を嘲笑うかのような、圧倒的な全力攻撃。

### S10 ハドマギリ
裂傷という「時限爆弾」を即座に爆発させる、シスイの代表的[切札](../rules.md)。

### S10 ウバラザキ
相手のエネルギー（[フレア](../rules.md#flare)）さえも裂傷で食いつぶす。

### S10 アブダグイ
いかなる窮地も裂傷として受け流す、驚異の対応札。

### S10 ヂーガデハド
シスイの狂気が頂点に達した時、すべてを無に帰す暗黒の刃。

## アンチメガミ・相性
- **得意**: 耐久力の低いメガミ、またはリソース供給が細いメガミ（[アキナ](23_akina.md)等とのリソース合戦）。
- **苦手**: 圧倒的バースト火力の[ユリナ](01_yurina.md)や、レンジロックの[ハツミ](17_hatsumi.md)。
- **対策**: 『茨道』で強引に詰め、『ハドマギリ』のコスパを活かした早めの決着を目指せ。

---

!!! note "出典"
    本ページの内容は「算鋸が強すぎたから解説してみた」（ぷれ）を主な根拠としています。
