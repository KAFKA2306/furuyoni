import { baseUrl, portraits } from './data.js';
const megamiList = [
    { no: "01", name: "ユリナ", role: "刀", keyword: "決死", feature: "ビートダウン / 高打点", desc: "シンプルかつ強力。間合3-4に潜り込み、重い一撃（月影落）を叩き込む。" },
    { no: "02", name: "サイネ", role: "薙刀", keyword: "八相", feature: "中距離 / カウンター", desc: "間合4-5での安定した攻撃と強力な対応札（氷雨細音の果ての果て）を持つ。" },
    { no: "03", name: "ヒミカ", role: "銃", keyword: "連火", feature: "コンボ / 遠距離", desc: "間合4-8から一方的に攻撃し、連火によるバーストダメージを狙う。" },
    { no: "04", name: "トコヨ", role: "扇", keyword: "境地", feature: "コントロール / 守り", desc: "鉄壁の防御を誇る。攻撃を無効化・反射し、相手の息切れを待つ。" },
    { no: "05", name: "オボロ", role: "忍", keyword: "設置", feature: "アグロ / 奇襲", desc: "設置カードを利用して手数を稼ぎ、相手を翻弄する。" },
    { no: "06", name: "ユキヒ", role: "傘", keyword: "開閉", feature: "柔軟 / 変幻自在", desc: "傘の状態で攻撃範囲が変化。隙を見て懐に潜り込む。" },
    { no: "07", name: "シンラ", role: "書", keyword: "計略", feature: "デバフ / メタ", desc: "相手の手札や山札を攻め、論破して行動を制限する。" },
    { no: "08", name: "ハガネ", role: "槌", keyword: "遠心", feature: "重量級 / 位置取り", desc: "移動を条件とする超火力（大天空クラッシュ）を持つ。" },
    { no: "09", name: "チカゲ", role: "毒", keyword: "毒", feature: "妨害 / 持久戦", desc: "相手に「毒カード」を送りつけ、手札を圧迫しつつダメージを与える。" },
    { no: "10", name: "クルル", role: "機巧", keyword: "機巧", feature: "コンボ / 構築", desc: "機構を組み立て、ド派手な効果（ビッグゴーレム）を発動させる。" },
    { no: "11", name: "サリヤ", role: "乗騎", keyword: "騎動/造花", feature: "ラッシュ / 変形", desc: "ライフやフレアを燃料にして機動力を高め、戦場を駆け巡る。" },
    { no: "12", name: "ライラ", role: "爪", keyword: "帯電", feature: "ストーム / 連撃", desc: "風と雷のゲージを溜め、手数を稼いで圧倒する。" },
    { no: "13", name: "ウツロ", role: "鎌/塵", keyword: "灰塵", feature: "レイトゲーム / 収奪", desc: "ダストが増える終盤に最強クラスになる。相手のリソースを奪う。" },
    { no: "14", name: "ホノカ", role: "旗", keyword: "守護", feature: "成長 / シナジー", desc: "精霊を開花させてカードを強化し、サポートもこなす。" },
    { no: "15", name: "コルヌ", role: "橇", keyword: "凍結", feature: "ロック / 妨害", desc: "相手のリソースを凍結させ、行動不能に追い込む。" },
    { no: "16", name: "ヤツハ", role: "鏡", keyword: "鏡映", feature: "コピー / カウンター", desc: "相手の攻撃をコピーしたり反射したりする。" }
];
export function renderMegamiRoster() {
    return `
        <div class="megami-grid">
            ${megamiList.map(m => `
                <div class="megami-card">
                    <div class="megami-header">
                        <span class="megami-no">No.${m.no}</span>
                        <h3 class="megami-name">${m.name}</h3>
                        <span class="megami-role">${m.role}</span>
                    </div>
                    <div class="megami-body">
                         <div class="megami-portrait-container">
                            <img src="${baseUrl}${portraits[m.name]}" alt="${m.name}" class="megami-portrait">
                        </div>
                        <div class="megami-info">
                            <p><strong>特徴:</strong> ${m.feature}</p>
                            <p><strong>キーワード:</strong> <span class="keyword">${m.keyword}</span></p>
                            <p class="megami-desc">${m.desc}</p>
                        </div>
                    </div>
                </div>
            `).join('')}
        </div>
    `;
}
