# ユリナ

<div class="megami-hud" style="display: grid; grid-template-columns: 100px 1fr; gap: 20px; background: rgba(0,0,0,0.05); padding: 20px; border-radius: 10px; border-left: 5px solid #d32f2f;">
  <img src="" width="100">
  <div class="hud-content">
    <div style="font-size: 1.5em; font-weight: bold; margin-bottom: 5px;">【刀】ユリナ / Season 10</div>
    <div style="display: flex; gap: 15px; font-size: 0.9em;">
      <span>難易度: ★☆☆☆☆</span>
      <span>[間合](../mechanics.md#range): 3-4</span>
      <span>タイプ: ビートダウン</span>
      <span style="color: #d32f2f; font-weight: bold;">S10 Meta: Tier 1 (Center)</span>
    </div>
  </div>
</div>

## S10 環境分析
```mermaid
graph LR
    A[アキナ弱体化] --> B(リソース確保の容易化)
    C[大型切札復権] --> D(月影落の圧倒的リーサル)
    B --> E[ユリナの安定性向上]
    D --> E
```

> [!CAUTION]
> **初心者が陥る致命的な罠**
> - **無計画な[決死](../mechanics.md#kesshi)**: [ライフ](../mechanics.md#life)3は敵のキルゾーン。対応札（浦波嵐・浮舟宿）が手元にない状態での[決死](../mechanics.md#kesshi)入りは敗北。
> - **[フレア](../mechanics.md#flare)の浪費**: 『月影落』(7)の圧力を失うことは、ユリナの勝率を50%捨てることに等しい。

## 戦略的タイムライン

### Phase 1: 開幕 (Turn 1-2)
- **目的**: [フレア](../mechanics.md#flare)の種を蒔き、[間合](../mechanics.md#range)3-4へ潜り込む。
- **推奨挙動**: 
    - [宿し](../mechanics.md#yadoshi) > [前進](../mechanics.md#advance)
    - 相手の[2/1]攻撃を[ライフ](../mechanics.md#life)で受け、[フレア](../mechanics.md#flare)転換。

### Phase 2: 中盤 (Turn 3-5)
- **目的**: 相手の[オーラ](../mechanics.md#aura)を『[![斬](../assets/images/card/cards/na_01_o_n/na_01_o_n_1.png)](../assets/images/card/cards/na_01_o_n/na_01_o_n_1.png){ .glightbox }』『[![圧気](../assets/images/card/cards/na_01_o_n/na_01_o_n_7.png)](../assets/images/card/cards/na_01_o_n/na_01_o_n_7.png){ .glightbox }』で剥がし、[ライフ](../mechanics.md#life)4-5へ追い込む。
- **決戦準備**: [ライフ](../mechanics.md#life)4付近で[集中力](../mechanics.md#focus)2を維持し、いつでも[決死](../mechanics.md#kesshi)からリーサルを狙える構えを取る。

### Phase 3: 終盤 (リーサル)
- **目的**: 『月影落』または『天音揺波の底力』による強制決着。
- **コンボ**: `足捌き(3→2) > 居合[決死] (4/3) > 月影落 (8/4)` - 合計[ライフ](../mechanics.md#life)貫通力絶大。

## [通常札](../mechanics.md)性能マトリクス

| カード名 | 主な役割 | 通常時 | [決死](../mechanics.md#kesshi)時 | S10 特記事項 |
| :--- | :--- | :---: | :---: | :--- |
| **[![斬](../assets/images/card/cards/na_01_o_n/na_01_o_n_1.png)](../assets/images/card/cards/na_01_o_n/na_01_o_n_1.png){ .glightbox }** | 主力削り | 3/1 | 3/2 | 基本性能の高さ。 |
| **[![一閃](../assets/images/card/cards/na_01_o_n/na_01_o_n_2.png)](../assets/images/card/cards/na_01_o_n/na_01_o_n_2.png){ .glightbox }** | [ライフ](../mechanics.md#life)奪取 | 2/2 | 3/3 | **リーサルパーツ**。 |
| **[![柄打ち](../assets/images/card/cards/na_01_o_n/na_01_o_n_3.png)](../assets/images/card/cards/na_01_o_n/na_01_o_n_3.png){ .glightbox }** | 妨害/加速 | 1/1 | 1/1 | **S10: ヒット時集中+1** |
| **[![居合](../assets/images/card/cards/na_01_o_n/na_01_o_n_4.png)](../assets/images/card/cards/na_01_o_n/na_01_o_n_4.png){ .glightbox }** | 防御粉砕 | 3/2 | 4/3 | [![足捌き](../assets/images/card/cards/na_01_o_n/na_01_o_n_5.png)](../assets/images/card/cards/na_01_o_n/na_01_o_n_5.png){ .glightbox }とのコンボ推奨。 |
| **[![足捌き](../assets/images/card/cards/na_01_o_n/na_01_o_n_5.png)](../assets/images/card/cards/na_01_o_n/na_01_o_n_5.png){ .glightbox }** | 位置調整 | 移動 | 移動 | **3→2の潜り込み**に必須。 |
| **[![気炎万丈](../assets/images/card/cards/na_01_o_n/na_01_o_n_6.png)](../assets/images/card/cards/na_01_o_n/na_01_o_n_6.png){ .glightbox }**| 火力バフ | 強化 | 強化 | 月影落の対応不可領域を拡大。 |
| **[![圧気](../assets/images/card/cards/na_01_o_n/na_01_o_n_7.png)](../assets/images/card/cards/na_01_o_n/na_01_o_n_7.png){ .glightbox }** | リソース破壊 | 納 | 納 | 相手の[オーラ](../mechanics.md#aura)管理を瓦解させる。 |

## [切札](../mechanics.md)：必殺の定義

| 名称 | コスト | 種別 | 解説 |
| :--- | :---: | :--- | :--- |
| **月影落** | 7 | 攻撃 | **フィニッシャー**。対応の有無、[ライフ](../mechanics.md#life)/[オーラ](../mechanics.md#aura)の択を強要する。 |
| **浦波嵐** | 3 | 対応 | **生命線**。[決死](../mechanics.md#kesshi)状態を安全に通過するためのクッション。 |
| **浮舟宿** | 2 | 行動 | **リソース補給**。[ダスト](../mechanics.md#dust)から[オーラ](../mechanics.md#aura)を増強し、判定勝ちへの導線。 |
| **底力** | 5 | 攻撃 | **逆転札**。最大[5/5]以上の[ライフ](../mechanics.md#life)ダメージを吐き出す。 |

## アンチメガミ・相性
- **得意**: 防御が薄い、または低速なメガミ（[サイネ](02_saine.md)などとの中距離戦）。
- **苦手**: 遠距離を維持し続ける「レンジロック」（[ハツミ](17_hatsumi.md)・[サリヤ](11_sariya.md)）。
- **対策**: 『[![足捌き](../assets/images/card/cards/na_01_o_n/na_01_o_n_5.png)](../assets/images/card/cards/na_01_o_n/na_01_o_n_5.png){ .glightbox }』を全力で回し、1回のチャンスで『月影落』を叩き込む「ワンチャンス」戦術へ移行せよ。
