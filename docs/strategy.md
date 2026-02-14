# 中級者向け戦略ガイド

基本ルールと初心者カリキュラムを終えたミコトへ、次のステップに進むためのガイドです。
ここでは、「なんとなく」プレイするのを卒業し、意図を持って勝利を手繰り寄せるための考え方を解説します。

## 0. 基礎メカニクスと用語の再確認

戦略を語る前に、中級者が勘違いしやすい、あるいは曖昧に覚えがちなルールを明確にしておきます。

### [間合](mechanics.md) (Ma-ai)
- 0〜10の整数値で表されます。基本的には、「[前進](mechanics.md)」で減り、「[後退](mechanics.md)」で増えます（達人の[間合](mechanics.md)い＝2は例外）。
- 多くの攻撃カードには適正[間合](mechanics.md)があり、その範囲内にいないと使用できません。

### ダメージ処理 (Damage Process)
攻撃が当たった時、ダメージを受ける側は「[ライフ](mechanics.md)」か「[オーラ](mechanics.md)」のどちらで受けるかを選びます（カード効果で指定がある場合を除く）。
- [オーラ](mechanics.md)受け: [オーラ](mechanics.md)から[ダスト](mechanics.md)へ結晶が移動します。[オーラ](mechanics.md)が足りない場合、選べません（[ライフ](mechanics.md)受けになります）。
- [ライフ](mechanics.md)受け: [ライフ](mechanics.md)から[フレア](mechanics.md)へ結晶が移動します。これが[切札](mechanics.md)の使用コストになります。

---

## 1. [眼前構築](mechanics.md)のセオリー

ふるよにの醍醐味である「[眼前構築](mechanics.md)」。相手の2柱を見てからデッキを組むこのフェーズで、勝負の5割が決まります。

### 相手の「最大値」を見積もる
デッキは「[通常札](mechanics.md)7枚、[切札](mechanics.md)3枚」で構築されます。このルールの中で、相手ができる「一番強い動き（ブン回り）」を想像しましょう。

- 相手のリーサルラインは？: [ユリナ](megami/index.md)なら「月影落」で6点前後、[ヒミカ](megami/index.md)なら「[![フルバースト](assets/images/card/cards/na_03_o_n/na_03_o_n_4.png)](assets/images/card/cards/na_03_o_n/na_03_o_n_4.png){ .glightbox }」で5〜8点。自分がどのくらい[ライフ](mechanics.md)を減らされたら危険域なのかを把握します。
- 相手の防御性能は？: [トコヨ](megami/index.md)の「久遠ノ花」があるなら、大技は通らない前提で「細かい攻撃を重ねる」構成にする必要があります。

### 自分の「勝ち筋」を決める
漫然と「強そうなカード」を7枚選ぶのではなく、「どうやって勝つか」のシナリオを持たせます。

1.  アグロプラン: 序盤から積極的に[前進](mechanics.md)・攻撃し、相手が準備を整える前に倒し切る。
2.  コントロールプラン: 相手の攻撃を[オーラ](mechanics.md)受けや対応で凌ぎ、[フレア](mechanics.md)を貯めて[切札](mechanics.md)の連打で逆転する。
3.  コンボプラン: 特定のカード（Ex. スカーレットイマジン、森羅判証）を揃えることを最優先し、揃った瞬間に決める。

「今回はこのプランで行く」と決めたら、そのプランに不要なカードは入れない勇気が必要です。

## 2. リソース管理の深化

### 「3-1」ドローと手札調整
毎ターン2枚引くこのゲームにおいて、手札調整は重要です。
基本的に、「3ターンに1回、[再構成](mechanics.md)（リシャッフル）が起きる」と覚えましょう。

- 初手は3枚: 先攻・後攻ともに、最初のターンは山札から3枚引きます。
- マリガン（引き直し）: ゲーム開始時に1度だけ行えます。任意の枚数を山札の底に戻し、同数を引きます。戻したカードは底に行くため、ゲーム序盤には引けません。
- 山札は7枚: 初手3枚 + (毎ターン2枚 × 2ターン) = 7枚。つまり、3ターン目の開始時には山札が尽きています。
- [再構成](mechanics.md)のコスト: 山札がない状態でカードを引く（または任意で行う）と[再構成](mechanics.md)が発生します。[ライフ](mechanics.md)に1ダメージを受け、捨て札と伏せ札を合わせて山札を作り直します。
- 伏せ札の活用: 不要なカードを伏せる（[基本動作](mechanics.md)）ことは、「次の[再構成](mechanics.md)を早める」行為でもあります。早くキーカードを引き込みたい時は、積極的に伏せて山札を回しましょう。

### [集中力](mechanics.md)と[ライフ](mechanics.md)の天秤
「[纏い](mechanics.md)（[オーラ](mechanics.md)回復）」や「[宿し](mechanics.md)（[フレア](mechanics.md)獲得）」は、基本的には[集中力](mechanics.md)で行うのが効率的です。
しかし、「[ライフ](mechanics.md)で受けるか、[オーラ](mechanics.md)で受けるか」の判断は常に問われます。

- [オーラ](mechanics.md)受け: 相手の追撃を防ぐために[オーラ](mechanics.md)を保つ。しかし、[オーラ](mechanics.md)が空になると、小さな攻撃（2/1など）が[ライフ](mechanics.md)に直撃します。
- [ライフ](mechanics.md)受け: あえて[ライフ](mechanics.md)で受けて[フレア](mechanics.md)を貯める（[宿し](mechanics.md)）。「肉を切らせて骨を断つ」戦法ですが、リーサル計算を誤ると即死します。

中級者の目安: [ライフ](mechanics.md)が4〜5になったら、いつ死んでもおかしくありません。ここからは徹底して[オーラ](mechanics.md)を維持し、[決死](mechanics.md)の覚悟で防御しましょう。

## 3. 「見えない情報」を読む

相手の手札や伏せ札を読むことで、対応の精度が劇的に上がります。

### 対応不可のタイミング
相手が「[集中力](mechanics.md)が0」で「手札が0〜1枚」の時、相手は全力で攻撃してきているため、防御（対応）手段を持っていない可能性が高いです。
このタイミングこそが、こちらの攻撃を通す最大のチャンスです。

### 捨て札からの逆算
相手の捨て札（トラッシュ）を確認しましょう。
「あの攻撃カードがまだ見えていない」＝「手札にある」か「山札の底」か「今回は採用していない」のどれかです。
特に[切札](mechanics.md)は、一度使えば基本的には戻ってきません。相手の[切札](mechanics.md)が透けた（使い切った）瞬間、強気に攻めることができます。


## ゲームプランと勝利の勘所

『桜降る代に決闘を』（ふるよに）において、どのように勝ち筋を描き、実行に移すのか。ルールとカード効果に基づいた戦略の核心を解説します。

### 1. 勝利の定義：[ライフ](mechanics.md)を0にする

このゲームの唯一の目標は、相手の**[ライフ](mechanics.md)を0**にすることです。
しかし、漫然と攻撃を振るだけでは勝てません。[ライフ](mechanics.md)を減らすには以下の2つのルートを意識する必要があります。

-   **攻撃による[ライフ](mechanics.md)ダメージ**: 攻撃カードの右側の数値（X/**Y**）で[ライフ](mechanics.md)を削る。
-   **[再構成](mechanics.md)ダメージ**: 相手が山札を引き切り、[再構成](mechanics.md)を行うたびに受ける1ダメージ。

#### 勘所：リーサル計算
相手の[ライフ](mechanics.md)が残り3〜4点になった瞬間が「勝負所」です。自分の手札、[集中力](mechanics.md)、そして[フレア](mechanics.md)（[切札](mechanics.md)）で、今この瞬間に[ライフ](mechanics.md)を削りきれるか（リーサル）を常に計算してください。

---

### 2. 資源の循環：[桜花結晶](mechanics.md)の法則

ふるよにの戦略の根幹は、**「[桜花結晶](mechanics.md)がどこからどこへ動くか」**を制御することにあります。

#### リソース・ループ
1.  **[オーラ](mechanics.md)を削る**: 攻撃を[オーラ](mechanics.md)で受けさせ、結晶を[ダスト](mechanics.md)へ送る。
2.  **[ライフ](mechanics.md)を削る**: [オーラ](mechanics.md)がない、あるいは防ぎきれない攻撃を[ライフ](mechanics.md)で受けさせ、結晶を[フレア](mechanics.md)へ送る。
3.  **[フレア](mechanics.md)を活用する**: [ライフ](mechanics.md)受けで得た[フレア](mechanics.md)をコストに、強力な**[切札](mechanics.md)**を放つ。

#### 勘所：ダメージ選択のジレンマ
攻撃を受けた際、「[オーラ](mechanics.md)で受けるか[ライフ](mechanics.md)で受けるか」の選択が勝敗を分けます。
-   **[オーラ](mechanics.md)受け**: 次の攻撃を防ぐ盾を維持するが、[フレア](mechanics.md)は増えない。
-   **[ライフ](mechanics.md)受け**: [フレア](mechanics.md)が増えて[切札](mechanics.md)が使えるようになるが、[ライフ](mechanics.md)が減り、敗北に近づく。

> [!IMPORTANT]
> **「あえて[ライフ](mechanics.md)で受けて、返しのターンに[切札](mechanics.md)で仕留める」**という判断が、中級者への第一歩です。

---

### 3. 距離の支配：[間合](mechanics.md)の管理

[間合](mechanics.md)は単なる数字ではなく、**そのメガミの「射程圏」**を表します。

-   **得意[間合](mechanics.md)を維持する**: 自分の強力な攻撃カードが使える距離（例：[ユリナ](megami/index.md)なら3-4、[ヒミカ](megami/index.md)なら5-10）をキープします。
-   **相手の得意[間合](mechanics.md)から逃げる**: 相手が攻撃できない距離へ、[基本動作](mechanics.md)（[後退](mechanics.md)・[纏い](mechanics.md)・[前進](mechanics.md)）で移動します。

---

### 4. ゲームの進行：3つのフェイズ

#### 序盤：準備と牽制（1〜2巡目）
-   **[宿し](mechanics.md)**で[フレア](mechanics.md)を最低限確保する。
-   相手の[オーラ](mechanics.md)を適度に削り、[ダスト](mechanics.md)を作る（自分の**[纏い](mechanics.md)**のため）。
-   手札を整え、強力なコンボが打てる準備をする。

#### 中盤：リソースの削り合い（[ライフ](mechanics.md) 7〜4）
-   互いに[ライフ](mechanics.md)を削り、[切札](mechanics.md)が使用可能になる。
-   [対応](mechanics.md)カードを構え、相手の大技を警戒する。

#### 終盤：リーサルの攻防（[ライフ](mechanics.md) 3以下）
-   [オーラ](mechanics.md)を5（上限）に保ち、[ライフ](mechanics.md)への致命傷を防ぐ。
-   **[再構成](mechanics.md)ダメージ**を考慮し、あえて[再構成](mechanics.md)せずに戦う判断も必要。
-   リソースを全て使い切り、相手の[ライフ](mechanics.md)を0に叩き込む。

---

### 5. 勝利のためのチェックリスト

- [ ] 相手の最大打点（どの[切札](mechanics.md)で何点飛んでくるか）を把握しているか？
- [ ] 自分の次のターンのドロー枚数を考慮して手札を調整したか？
- [ ] 無駄な「[前進](mechanics.md)」で、相手が得意な近距離に飛び込んでいないか？
- [ ] [フレア](mechanics.md)は足りているか？ [宿し](mechanics.md)すぎで[オーラ](mechanics.md)がスカスカになっていないか？

このゲームプランを意識することで、あなたの決闘は「運」から「戦略」へと進化します。


## シーズン10 メタレポート

### 環境概要 (2026年 - S10-2期)

現在は2026年2月、長きにわたる**シーズン10 (S10)** が成熟し、**S10-2** へと移行している段階です。
2025年末の「シーズン10総括」および「ぎふよに大決戦」の結果を踏まえた、最新のメタゲーム分析です。

#### Tier 1：環境の定義 (S10総括)

「強いメガミを強く使う」ことが肯定される、パワー偏重の環境が続いています。

- **[ヒミカ](megami/03_himika.md) / [ウツロ](megami/13_utsuro.md)** (銃鎌):
    - 2025年大規模イベント優勝の要因。
    - 「レッドバレット」規制後も、相方を変えたり構築を工夫することで環境の頂点に立ち続けています。
- **[サリヤ](megami/11_sariya.md) (Ride) 軸**:
    - S10中期から圧倒的な使用率を誇るメタの中心。
    - 「Thallya's Masterpiece」によるリソース優位と「Waving Edge」の機動力が、あらゆる対面に対して高水準な回答を持っています。
- **3柱の傾向 (Complete)**:
    - [ハガネ](megami/08_hagane.md) (Hammer) や [アキナ](megami/index.md) (Abacus) を含めた「グッドスタッフ」構成が主流。
    - 特定のギミックに特化するよりも、カードパワーの高いメガミを組み合わせ、対応力で押し切る構築が結果を残しています。

#### 環境のカウンター & 注目株

- **[ミズキ](megami/index.md) (Helm)**:
    - Tier 1 (サリヤ・シスイ等) に対する明確な回答。
    - 徹底したメタ読みと「戦場の極意」によるケア強要で、トーナメントシーンでの安定感が非常に高いです。
- **異端の入賞**:
    - [オボロ](megami/05_oboro.md)A2 / [ハガネ](megami/08_hagane.md) / [クルル](megami/10_kururu.md) といった、一見「わからん殺し」に見える構成も上位に入賞。
    - メタ外からの刺突が機能する余地は残されており、練度による突破が証明されています。

### メトリクス & 統計 (2026年 Outlook)

| メトリクス項目 | 内容・動向 |
| :--- | :--- |
| **規制の影響** | 銃鎌の「レッドバレット」規制は継続中ですが、ヒミカ自体の採用率は依然高水準です。 |
| **メタの流動** | S10-2への移行に伴い、ハガネ/サリヤ中心の環境から、より多様な「3柱目」の模索が始まっています。 |
| **イベント指標** | 2026年4月「桜端の大決闘祭」に向け、VRChat環境を含めた研究が加速中。 |

!!! note "出典"
    本分析は[note: シーズン10反省会](https://note.com/herbivores0422/n/n1e76e143b0b9)および[ikariのふるよに図書館](https://ikari2642.hatenablog.com/entry/gifuyoni3)のレポートを統合・要約したものです。


## ペア攻略一覧

1. <span id="yurina-saine"></span>刀薙（[ユリナ](megami/01_yurina.md)／[サイネ](megami/02_saine.md)）
   中距離（[間合](mechanics.md)3〜5）で「大型[切札](mechanics.md)2枚＋条件達成での火力跳ね上がり」を押し付けて圧殺する、王道の高打点ミッドレンジです。[決死](mechanics.md)や[八相](mechanics.md)の条件が噛むと打点が異常値になり、相手の受けの設計を破壊します。一方で機動力が乏しいので、遠距離レンジロックや超近距離クリンチに寄せられるとプランが崩れやすいです。([Hikari Fryn][2])


<div class="grid cards" markdown>

-   ![ユリナ](assets/images/chara/ico-01.png)

-   ![サイネ](assets/images/chara/ico-02.png)

</div><details><summary>[ユリナ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_a1_n_1.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_a1_n_6.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_a2_n_3.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_a2_n_7.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_1.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_2.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_3.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_4.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_5.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_6.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_7.png)

</div></details>
<details><summary>[サイネ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a1_n_1.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a1_n_6.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a2_n_2.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a2_n_7.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_1.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_2.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_3.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_4.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_5.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_6.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_7.png)

</div></details>

2. <span id="yurina-tokoyo"></span>刀扇（[ユリナ](megami/01_yurina.md)／[トコヨ](megami/04_tokoyo.md)）
   [ユリナ](megami/01_yurina.md)の素直な殴り合い性能に、[トコヨ](megami/04_tokoyo.md)の「対応（カウンター）や安定性」を足して、攻防バランスを“丸く強く”した型です。相手に合わせて構築を調整しやすく、初心者でも上級者でも握り続けられる基礎体力があります。「困ったら刀扇」になりやすい代表格です。([ふるよにしたいヤシロの書][3])


<div class="grid cards" markdown>

-   ![ユリナ](assets/images/chara/ico-01.png)

-   ![トコヨ](assets/images/chara/ico-04.png)

</div><details><summary>[ユリナ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_a1_n_1.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_a1_n_6.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_a2_n_3.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_a2_n_7.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_1.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_2.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_3.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_4.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_5.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_6.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_7.png)

</div></details>
<details><summary>[トコヨ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_a1_n_1.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_a1_n_4.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_a2_n_2.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_1.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_2.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_3.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_4.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_5.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_6.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_7.png)

</div></details>

3. <span id="saine-tokoyo"></span>薙扇（[サイネ](megami/02_saine.md)／[トコヨ](megami/04_tokoyo.md)）
   防御手段が非常に厚く、条件（[八相](mechanics.md)・[境地](mechanics.md)）を満たすと攻防が高水準にまとまり、対応札の多さで相手にケアを強制する“万能コントロール寄り”です。回れば多くの相手に互角以上を取りやすい反面、条件管理の精度が要求され、プレイが雑だとただ遅いデッキになりがちです。([Hikari Fryn][4])


<div class="grid cards" markdown>

-   ![サイネ](assets/images/chara/ico-02.png)

-   ![トコヨ](assets/images/chara/ico-04.png)

</div><details><summary>[サイネ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a1_n_1.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a1_n_6.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a2_n_2.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a2_n_7.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_1.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_2.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_3.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_4.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_5.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_6.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_7.png)

</div></details>
<details><summary>[トコヨ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_a1_n_1.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_a1_n_4.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_a2_n_2.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_1.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_2.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_3.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_4.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_5.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_6.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_7.png)

</div></details>

4. <span id="himika-tokoyo"></span>銃扇（[ヒミカ](megami/03_himika.md)／[トコヨ](megami/04_tokoyo.md)）
   序盤の[連火](mechanics.md)を絡めた攻め（[ヒミカ](megami/03_himika.md)）と、近中距離のコントロールや遠距離の[切札](mechanics.md)圧（[トコヨ](megami/04_tokoyo.md)）を両立し、「近くも遠くもやれる」せいで相手の対策方針を迷わせる型です。強い出し方は“どちらかに寄せて尖らせる”ことで、バランス取り過ぎると決め手が薄くなります。([Hikari Fryn][5])


<div class="grid cards" markdown>

-   ![ヒミカ](assets/images/chara/ico-03.png)

-   ![トコヨ](assets/images/chara/ico-04.png)

</div><details><summary>[ヒミカ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_a1_n_2.png)

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_a1_n_5.png)

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_o_n_1.png)

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_o_n_2.png)

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_o_n_3.png)

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_o_n_4.png)

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_o_n_5.png)

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_o_n_6.png)

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_o_n_7.png)

</div></details>
<details><summary>[トコヨ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_a1_n_1.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_a1_n_4.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_a2_n_2.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_1.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_2.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_3.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_4.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_5.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_6.png)

-   ![Card](assets/images/card/cards/na_04_o_n/na_04_o_n_7.png)

</div></details>

5. <span id="saine-himika"></span>薙銃（[サイネ](megami/02_saine.md)／[ヒミカ](megami/03_himika.md)）
   「遠距離レンジロック」「[後退](mechanics.md)しながらの攻撃」「[連火](mechanics.md)の打点ブースト」などで、1巡目と中盤以降に“まとまった攻撃の波”を2回作って勝つプランが代表的です。相手は距離と受けの両方にケアが必要で、ミスると一気に[ライフ](mechanics.md)が溶けます。([Hikari Fryn][6])


<div class="grid cards" markdown>

-   ![サイネ](assets/images/chara/ico-02.png)

-   ![ヒミカ](assets/images/chara/ico-03.png)

</div><details><summary>[サイネ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a1_n_1.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a1_n_6.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a2_n_2.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a2_n_7.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_1.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_2.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_3.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_4.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_5.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_6.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_7.png)

</div></details>
<details><summary>[ヒミカ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_a1_n_2.png)

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_a1_n_5.png)

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_o_n_1.png)

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_o_n_2.png)

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_o_n_3.png)

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_o_n_4.png)

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_o_n_5.png)

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_o_n_6.png)

-   ![Card](assets/images/card/cards/na_03_o_n/na_03_o_n_7.png)

</div></details>

6. <span id="yurina-oboro"></span>刀忍（[ユリナ](megami/01_yurina.md)／[オボロ](megami/05_oboro.md)）
   近距離（特に[間合](mechanics.md)2付近）でのビートダウンが極めて強く、[オボロ](megami/05_oboro.md)の[設置](mechanics.md)で利得を稼ぎつつ、[ユリナ](megami/01_yurina.md)の[切札](mechanics.md)で決め切る“シンプルでパワフル”な型です。弱点は極端で、遠距離レンジロックやクリンチ（[間合](mechanics.md)0に押し込む）に寄せられると攻撃が振れなくなりやすいです。([Hikari Fryn][7])


<div class="grid cards" markdown>

-   ![ユリナ](assets/images/chara/ico-01.png)

-   ![オボロ](assets/images/chara/ico-05.png)

</div><details><summary>[ユリナ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_a1_n_1.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_a1_n_6.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_a2_n_3.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_a2_n_7.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_1.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_2.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_3.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_4.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_5.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_6.png)

-   ![Card](assets/images/card/cards/na_01_o_n/na_01_o_n_7.png)

</div></details>
<details><summary>[オボロ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_a1_n_2.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_a1_n_3.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_a2_n_1.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_o_n_1.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_o_n_2.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_o_n_3.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_o_n_4.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_o_n_5.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_o_n_6.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_o_n_7.png)

</div></details>

7. <span id="oboro-yukihi"></span>忍傘（[オボロ](megami/05_oboro.md)／[ユキヒ](megami/06_yukihi.md)）
   [設置](mechanics.md)で利得を稼ぐ[オボロ](megami/05_oboro.md)と、傘の[開閉](mechanics.md)で得意[間合](mechanics.md)が変わる[ユキヒ](megami/06_yukihi.md)を合わせ、クロック的に削りながら終盤にリーサルを作る型が有名です。特定対面（レンジロック相手など）への回答として刺さりやすく、回り始めると相手が追いつけない展開になりますが、ループが止まる条件（大きい被弾、[後退](mechanics.md)不能など）を踏むと一気に破綻します。([Hikari Fryn][8])


<div class="grid cards" markdown>

-   ![オボロ](assets/images/chara/ico-05.png)

-   ![ユキヒ](assets/images/chara/ico-06.png)

</div><details><summary>[オボロ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_a1_n_2.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_a1_n_3.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_a2_n_1.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_o_n_1.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_o_n_2.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_o_n_3.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_o_n_4.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_o_n_5.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_o_n_6.png)

-   ![Card](assets/images/card/cards/na_05_o_n/na_05_o_n_7.png)

</div></details>
<details><summary>[ユキヒ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_a1_n_2.png)

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_a1_n_4.png)

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_o_n_1.png)

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_o_n_2.png)

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_o_n_3.png)

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_o_n_4.png)

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_o_n_5.png)

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_o_n_6.png)

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_o_n_7.png)

</div></details>

8. <span id="saine-shinra"></span>「書」[シンラ](megami/07_shinra.md)系（例：薙書＝[サイネ](megami/02_saine.md)／[シンラ](megami/07_shinra.md)、ほか[シンラ](megami/07_shinra.md)核）
   [シンラ](megami/07_shinra.md)は「相手のデッキギミック破壊」「悠長なプランの否定」「レンジロック補助・対抗」など、“ふるよにの基本構造から外れた勝ち筋”を取り締まるのが強みで、相方の火力補助やサブ火力も担えます。薙書のように、相方でビートもコントロールもカバーできる組み合わせはデッキタイプの射程が広く、対面適応力が高いのが売りです。([へくとぱ雑文投棄所][9])

<div class="grid cards" markdown>

-   ![サイネ](assets/images/chara/ico-02.png)

-   ![シンラ](assets/images/chara/ico-07.png)

</div><details><summary>[サイネ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a1_n_1.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a1_n_6.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a2_n_2.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a2_n_7.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_1.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_2.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_3.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_4.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_5.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_6.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_7.png)

</div></details>
<details><summary>[シンラ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_07_o_n/na_07_a1_n_2.png)

-   ![Card](assets/images/card/cards/na_07_o_n/na_07_a1_n_7.png)

-   ![Card](assets/images/card/cards/na_07_o_n/na_07_o_n_1.png)

-   ![Card](assets/images/card/cards/na_07_o_n/na_07_o_n_2.png)

-   ![Card](assets/images/card/cards/na_07_o_n/na_07_o_n_3.png)

-   ![Card](assets/images/card/cards/na_07_o_n/na_07_o_n_4.png)

-   ![Card](assets/images/card/cards/na_07_o_n/na_07_o_n_5.png)

-   ![Card](assets/images/card/cards/na_07_o_n/na_07_o_n_6.png)

-   ![Card](assets/images/card/cards/na_07_o_n/na_07_o_n_7.png)

</div></details>

9. <span id="saine-yukihi"></span>薙傘（[サイネ](megami/02_saine.md)／[ユキヒ](megami/06_yukihi.md)）
   [ユキヒ](megami/06_yukihi.md)の「閉」攻撃で[サイネ](megami/02_saine.md)の隙を埋めつつ、[間合](mechanics.md)5-7を維持して一方的に殴り続けるミッドレンジ構成。[サイネ](megami/02_saine.md)のリソース不足を[ユキヒ](megami/06_yukihi.md)が補い、[八相](mechanics.md)状態の火力を最大限に活かします。やや決定力に欠けるため、[切札](mechanics.md)の通し場所を見極める必要があります。([THTF's DustBox][10])

<div class="grid cards" markdown>

-   ![サイネ](assets/images/chara/ico-02.png)

-   ![ユキヒ](assets/images/chara/ico-06.png)

</div><details><summary>[サイネ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a1_n_1.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a1_n_6.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a2_n_2.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_a2_n_7.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_1.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_2.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_3.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_4.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_5.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_6.png)

-   ![Card](assets/images/card/cards/na_02_o_n/na_02_o_n_7.png)

</div></details>
<details><summary>[ユキヒ](megami/index.md) Cards</summary>
<div class="grid cards" markdown>

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_a1_n_2.png)

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_a1_n_4.png)

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_o_n_1.png)

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_o_n_2.png)

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_o_n_3.png)

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_o_n_4.png)

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_o_n_5.png)

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_o_n_6.png)

-   ![Card](assets/images/card/cards/na_06_o_n/na_06_o_n_7.png)

</div></details>


### その他の注目シナジー (Brief Mentions)

#### 10. 刀騎（[ユリナ](megami/index.md)／[サリヤ](megami/index.md)）
[サリヤ](megami/index.md)の「[騎動](mechanics.md)」で[間合](mechanics.md)を一気に詰め、[ユリナ](megami/index.md)の重い一撃を叩き込むアグロ〜ミッドレンジ構成です。機動力と破壊力を兼ね備えています。

#### 10. 爪忍（[ライラ](megami/index.md)／[オボロ](megami/index.md)）
[オボロ](megami/index.md)の手数の多さ（[設置](mechanics.md)攻撃など）で[ライラ](megami/index.md)の[帯電](mechanics.md)ゲージを高速で溜め、後半に圧倒的な火力で押し切るコンボ色の強いビートダウンです。

#### 11. [毒](mechanics.md)氷（[チカゲ](megami/09_chikage.md)／[コルヌ](megami/15_korunu.md)）
[毒](mechanics.md)で手札を封じ、[凍結](mechanics.md)で[オーラ](mechanics.md)を封じる「完全ロック」を狙います。ハマれば相手は何もできずに窒息しますが、自身の火力が低めな点が課題です。

#### 12. [毒](index.md)鏡（[チカゲ](megami/09_chikage.md)／[ヤツハ](megami/16_yatsuha.md)）
[ヤツハ](megami/index.md)の『[寄花](megami/cards.md#yatsuha)』と[チカゲ](megami/index.md)の『[毒霧](megami/cards.md#chikage)』を組み合わせ、高速で山札を汚染するコントロール型です。
相手の山札を[毒](mechanics.md)で死滅させ、[ヤツハ](megami/index.md)の自傷ダメージを最小限に抑えながら、相手のリソースを根こそぎ奪い取ります。
([ブログ参照](https://main-bakafire.ssl-lolipop.jp/furuyoni/na/))
