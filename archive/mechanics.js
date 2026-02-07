export const mechanicsContent = `
<div class="rules-container">
    <section class="rules-section">
        <h2>コアコンセプト</h2>
        <p>ふるよにをプレイする上で欠かせない用語の解説です。</p>
        
        <h3>1. リソース（桜花結晶）</h3>
        <ul class="rules-list">
            <li><strong>ライフ</strong>: プレイヤーの体力。通常は10です。0になると敗北します。</li>
            <li><strong>オーラ</strong>: プレイヤーを守る盾。ダメージを代わりに受けます（上限5）。</li>
            <li><strong>フレア</strong>: 切札を使用するためのコスト。宿しやダメージで溜まります。</li>
            <li><strong>間合（まあい）</strong>: プレイヤー間の距離。基本開始距離は10。</li>
            <li><strong>ダスト</strong>: 捨て札置き場にある結晶。</li>
        </ul>

        <h3>2. カードの種類</h3>
        <ul class="rules-list">
            <li><strong>通常札</strong>（緑）: デッキに7枚。山札から引いて使用。</li>
            <li><strong>切札</strong>（赤）: デッキに3枚。フレアを支払っていつでも使用可能。</li>
        </ul>

        <h3>3. 基本動作</h3>
        <p>1「集中力」または手札1枚を消費して行います。</p>
        <ul class="rules-list">
            <li><strong>前進</strong>: 間合→オーラ（間合2より大きい時）</li>
            <li><strong>後退</strong>: オーラ→間合</li>
            <li><strong>纏い</strong>: ダスト→オーラ</li>
            <li><strong>宿し</strong>: オーラ→フレア</li>
        </ul>
    </section>

    <section class="rules-section">
        <h2>ゲームの流れ</h2>
        
        <h3>フェイズ1: 眼前構築</h3>
        <p>相手の2柱を見てからデッキを組みます。</p>
        <ul>
            <li>通常札 7枚</li>
            <li>切札 3枚</li>
        </ul>

        <h3>フェイズ2: 決闘開始</h3>
        <p><strong>初期配置</strong>: ライフ10 / オーラ3 / 間合10 / フレア0 / 手札3枚</p>

        <h4>ターンの進行</h4>
        <ol class="rules-list">
            <li><strong>開始フェイズ</strong>: 集中力+1、再構成（任意/山札0）、ドロー2枚</li>
            <li><strong>メインフェイズ</strong>: 基本動作、カード使用、切札使用</li>
            <li><strong>終了フェイズ</strong>: 手札上限調整（2枚）、終了時効果</li>
        </ol>

        <h3>勝利条件</h3>
        <ul>
            <li>相手のライフを0にする</li>
            <li>相手が再構成ダメージでライフ0になる</li>
        </ul>
    </section>
</div>
`;
