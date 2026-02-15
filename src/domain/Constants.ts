import path from 'path';

export const PROJECT_ROOT = path.resolve(__dirname, '../../');
export const DOCS_DIR = path.join(PROJECT_ROOT, 'docs');

export const BLACKLIST = new Set([
    "役割", "Role", "Range", "工廠", "燃焼", "凍結", "帯電", "機動",
    "騎動", "鬱積", "徹底抗戦", "神座渡", "あたらよ", "切札", "通常札",
    "ライフ", "オーラ", "フレア", "ダスト", "間合", "集中力",
    "攻撃", "行動", "付与", "対応", "全力", "特殊"
]);
