# ヒミカ

<div class="megami-header" style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
  <img src="../assets/images/chara/ico-03.png" width="100">
  <div class="megami-meta">
    <ul>
      <li><strong>権能</strong>: 銃 (Gun)</li>
      <li><strong>難易度</strong>: ★★☆☆☆</li>
      <li><strong>得意[間合](../mechanics.md#range)</strong>: 5-10</li>
      <li><strong>S10 Meta Tier</strong>: <span style="color: #ff9800; font-weight: bold;">A (Regulation Watch)</span></li>
    </ul>
  </div>
</div>

!!! info "彼方より降り注ぐ、紅蓮の弾丸"
    シーズン10においても、[間合](../mechanics.md#range)10からの支配力は健在。特に「銃鎌」「銃扇」などのペアにおける爆発力は、[眼前構築](../mechanics.md#construction)段階で相手に対策を強要するほどの圧力を誇ります。

---

## 軌跡とSeason 10の環境

ヒミカは「速攻」と「レンジロック」の二面性を持つメガミです。S10環境では、大型[切札](../mechanics.md)の復権により、それらが起動する前にゲームを終わらせる「アンチ・コントロール」としての価値が高まっています。

```mermaid
graph TD
    A[ヒミカ] --> B{戦術プラン}
    B -- 遠距離: 狙撃 --> C[レンジロック (銃扇)]
    B -- 速攻: 爆撃 --> D[OTKバースト (銃鎌)]
    C --> E[近接ビートダウンを完封]
    D --> F[準備型コントロールを粉砕]
    E --> G[S10 Meta: Tier A]
    F --> G
```

---

## 物語の起源：ヒミカ

> 「情熱は弾丸となって、天をも焦がすのよ！」

ヒミカは、かつて銃を手に戦場の空を駆けた熱き魂の具現です。
彼女の起源は、飽くなき好奇心と「速さ」への渇望にあります。彼女が操る紅蓮の銃火は、単なる破壊の道具ではなく、停滞した世界を打ち破るための情熱の輝きです。
物語において常に台風の目となる彼女は、その[連火](../mechanics.md#renka)の如く、連続する閃光で戦場を圧倒します。

---

## 初心者が陥りやすい罠

!!! caution "弾切れ（ガス欠）"
    ヒミカの最大の敵は自分自身です。序盤に気持ちよく『シュート』や『ラピッドファイア』を連射しすぎると、[再構成](../mechanics.md#reconstruction)直後の大事な場面で手札・山札がなくなり、何もできないターンが生まれます。**「撃つターン」と「溜めるターン」を明確に分けましょう。**

!!! warning "安易な[間合](../mechanics.md#range)接近"
    ヒミカは[間合](../mechanics.md#range)0-4においては無力に近い存在です（『[![クリムゾンゼロ](../assets/images/card/cards/na_03_o_s/na_03_o_s_4.png)](../assets/images/card/cards/na_03_o_s/na_03_o_s_4.png){ .glightbox }』採用時を除く）。相手に[前進](../mechanics.md#advance)リソースを与えないよう、無駄な攻撃を控えて[間合](../mechanics.md#range)10を維持する「待ち」の姿勢も重要です。

---

## 戦略的タイムライン

### バースト型 (OTK狙い)
| 局面 | 目標 | 推奨アクション |
| :--- | :--- | :--- |
| **序盤** | 準備 | [間合](../mechanics.md#range)10で『バックステップ』確保。[宿し](../mechanics.md#yadoshi)で[フレア](../mechanics.md#flare)を貯める。 |
| **中盤** | パーツ集め | キーカード（スカーレットイマジン等）を手札に揃える。攻撃は最低限。 |
| **終盤** | 決着 | 『[![レッドバレット](../assets/images/card/cards/na_03_o_s/na_03_o_s_1.png)](../assets/images/card/cards/na_03_o_s/na_03_o_s_1.png){ .glightbox }』『マグナムカノン』を一気に吐き出し、1ターンで8〜10点を削り切る。 |

### レンジロック型 (完封狙い)
| 局面 | 目標 | 推奨アクション |
| :--- | :--- | :--- |
| **序盤** | 剥がし | 『シュート』『[![フルバースト](../assets/images/card/cards/na_03_o_n/na_03_o_n_4.png)](../assets/images/card/cards/na_03_o_n/na_03_o_n_4.png){ .glightbox }』で相手の[オーラ](../mechanics.md#aura)を削る。 |
| **中盤** | 拘束 | 相手が[前進](../mechanics.md#advance)しようとして払った[オーラ](../mechanics.md#aura)を再び射撃で奪う。 |
| **終盤** | 詰み | 相手のリソースが枯渇したところで、一方的に[ライフ](../mechanics.md#life)を奪う。 |

---

## [通常札](../mechanics.md)性能マトリクス

| カード名 | 役割 | 適正[間合](../mechanics.md#range) | ダメージ | S10 評価 |
| :--- | :--- | :---: | :---: | :--- |
| **シュート** | 基本射撃 | 4-10 | 2/1 | ★★★★★ (万能) |
| **ラピッドファイア** | [連火](../mechanics.md#renka)始動 | 6-8 | 2/1 | ★★★★☆ (手数) |
| **マグナムカノン** | メイン火力 | 5-8 | 3/2 | ★★★★★ (最重要) |
| **フルバースト** | 範囲制圧 | 5-10 | 3/1 | ★★★★☆ (対多数) |
| **バックステップ** | 離脱/ドロー | - | - | ★★★★★ (潤滑油) |
| **バックドラフト** | 火力バフ | - | - | ★★★☆☆ (コンボ用) |
| **スモーク** | 防御剥がし | - | - | ★★☆☆☆ (環境依存) |

---

## [通常札](../mechanics.md)の詳細解説

### N1 シュート
[![シュート](../assets/images/card/cards/na_03_o_n/na_03_o_n_1.png)](../assets/images/card/cards/na_03_o_n/na_03_o_n_1.png){ .glightbox }

至近距離までカバーする汎用札。適正[間合](../mechanics.md#range)の広さゆえに腐ることがなく、[連火](../mechanics.md#renka)のカウント稼ぎとしても優秀です。

### N2 ラピッドファイア
[![ラピッドファイア](../assets/images/card/cards/na_03_o_n/na_03_o_n_2.png)](../assets/images/card/cards/na_03_o_n/na_03_o_n_2.png){ .glightbox }

[連火](../mechanics.md#renka)条件を満たすことで「手札に戻る（※要確認）」または「再使用」などの恩恵を受け、実質手札消費なしでダメージを稼げます。

### N3 マグナムカノン
[![マグナムカノン](../assets/images/card/cards/na_03_o_n/na_03_o_n_3.png)](../assets/images/card/cards/na_03_o_n/na_03_o_n_3.png){ .glightbox }

[ライフ](../mechanics.md#life)受けを強要させる3/2。ヒミカのダメージソースの要であり、これをいかに[ライフ](../mechanics.md#life)に通すかが勝負です。

### N4 フルバースト
[![フルバースト](../assets/images/card/cards/na_03_o_n/na_03_o_n_4.png)](../assets/images/card/cards/na_03_o_n/na_03_o_n_4.png){ .glightbox }

[連火](../mechanics.md#renka)達成時の追加効果が凶悪。相手のリソース（[オーラ](../mechanics.md#aura)・[ライフ](../mechanics.md#life)・[フレア](../mechanics.md#flare)・[ダスト](../mechanics.md#dust)）全てに干渉し、盤面を崩壊させます。

### N5 バックステップ
[![バックステップ](../assets/images/card/cards/na_03_o_n/na_03_o_n_5.png)](../assets/images/card/cards/na_03_o_n/na_03_o_n_5.png){ .glightbox }

[間合](../mechanics.md#range)を離しつつカードを引く、攻防一体のスキル。「攻めながら逃げる」ヒミカの動きを支える心臓部です。

### N6 バックドラフト
[![バックドラフト](../assets/images/card/cards/na_03_o_n/na_03_o_n_6.png)](../assets/images/card/cards/na_03_o_n/na_03_o_n_6.png){ .glightbox }

次の攻撃を強化。[決死](../mechanics.md#kesshi)でなくとも4/3の『マグナムカノン』を作り出せる、バーストダメージの起爆剤です。

### N7 スモーク
[![スモーク](../assets/images/card/cards/na_03_o_n/na_03_o_n_7.png)](../assets/images/card/cards/na_03_o_n/na_03_o_n_7.png){ .glightbox }

相手の[オーラ](../mechanics.md#aura)を結晶ごと排除（納）する妨害札。防御が堅い相手への突破口として機能します。

---

## [切札](../mechanics.md)の詳細解説

### S1 レッドバレット
[![レッドバレット](../assets/images/card/cards/na_03_o_s/na_03_o_s_1.png)](../assets/images/card/cards/na_03_o_s/na_03_o_s_1.png){ .glightbox }

**コスト0**の[3/1]。リソース消費なしで打てるため、リーサル計算が非常に計算しやすくなります。最後の一押しに。

### S2 スカーレットイマジン
[![スカーレットイマジン](../assets/images/card/cards/na_03_o_s/na_03_o_s_2.png)](../assets/images/card/cards/na_03_o_s/na_03_o_s_2.png){ .glightbox }

**コスト3**。手札を超大量に確保する、ヒミカ最強のコンボ始動パーツ。ここから全ての悪夢が始まります。

### S3 ルルララリ
[![ルルララリ](../assets/images/card/cards/na_03_o_s/na_03_o_s_3.png)](../assets/images/card/cards/na_03_o_s/na_03_o_s_3.png){ .glightbox }

**コスト4**。特殊勝利や盤面破壊をもたらす、ロマンと実用を兼ねた大技。

### S4 クリムゾンゼロ
[![クリムゾンゼロ](../assets/images/card/cards/na_03_o_s/na_03_o_s_4.png)](../assets/images/card/cards/na_03_o_s/na_03_o_s_4.png){ .glightbox }

**コスト5**。弱点である[間合](../mechanics.md#range)0-2をカバーする、対クリンチ最終兵器。「クリムゾンゆらりび」の相方としても著名です。

---

## おすすめの組み合わせ

### [トコヨ](04_tokoyo.md) (銃扇)
**「完璧なるレンジロック」**
[トコヨ](04_tokoyo.md)の防御力で時間を稼ぎ、ヒミカが理想的な手札を揃えるまで耐える構成。

### [ユキヒ](06_yukihi.md) (銃傘)
**「全域支配の弾幕」**
遠距離はヒミカ、中近距離は[ユキヒ](06_yukihi.md)が担当。どの[間合](../mechanics.md#range)も死角なし。

### [サイネ](02_saine.md) (銃薙)
**「中遠距離の暴力」**
ヒミカで荒らし、サイネの『八相』で刈り取る。攻撃的なシナジーが強力。

---

## 関連リンク
- [全カードリスト](cards.md#himika)
- [基本ルール](../mechanics.md)
