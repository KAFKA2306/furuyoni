import path from 'path';
import { Config } from '../domain/Config';
import { FileSystemAdapter } from '../infrastructure/FileSystemAdapter';
import { MappingService } from '../domain/MappingService';
import { PROJECT_ROOT, DOCS_DIR } from '../domain/Constants';

export class SyncCards {
    constructor(private config: Config) { }

    execute(): void {
        const outputCardsPath = path.join(PROJECT_ROOT, this.config.paths.output_cards);
        const cardMap = MappingService.buildCardMap();
        const megamiMap = MappingService.extractMegamiMapping();

        const idToName: { [id: string]: string } = {};
        for (const [name, relPath] of Object.entries(megamiMap)) {
            const match = relPath.match(/(\d+)_/);
            if (match) {
                idToName[match[1]] = name;
            }
        }

        const cardImagesDir = path.join(DOCS_DIR, 'assets/images/card/cards');
        const megamiData: { [id: string]: { [version: string]: { n: Set<number>, s: Set<number>, folders: Set<string> } } } = {};

        if (FileSystemAdapter.exists(cardImagesDir)) {
            for (const file of FileSystemAdapter.walkSync(cardImagesDir)) {
                if (!file.endsWith('.png')) continue;
                const filename = path.basename(file);
                const match = filename.match(/na_(\d+)_([oa]\d*)_([ns])_(\d+)\.png/);
                if (match) {
                    const [_, id, version, type, index] = match;
                    const idx = parseInt(index);
                    const folder = path.dirname(path.relative(cardImagesDir, file));

                    if (!megamiData[id]) megamiData[id] = {};
                    if (!megamiData[id][version]) megamiData[id][version] = { n: new Set(), s: new Set(), folders: new Set() };
                    
                    if (type === 'n') megamiData[id][version].n.add(idx);
                    if (type === 's') megamiData[id][version].s.add(idx);
                    megamiData[id][version].folders.add(folder);
                }
            }
        }

        let out = "# 全カード一覧\n\n";
        out += "各メガミのカードセット（通常札7枚＋切札4枚）を一覧できます。アナザー版の共通カードは透過表示されています。\n\n";

        const ids = Object.keys(idToName).sort();

        for (const id of ids) {
            const name = idToName[id];
            let headerAttr = "";
            const megamiFile = megamiMap[name];
            if (megamiFile) {
                const fname = path.basename(megamiFile);
                const mMatch = fname.match(/\d+_(\w+)\.md/);
                if (mMatch) {
                    headerAttr = ` {: #${mMatch[1]} }`;
                }
            }

            out += `## ${name}${headerAttr}\n\n`;

            const versions = megamiData[id] ? Object.keys(megamiData[id]).filter(v => {
                if (v === 'o') return true;
                return (megamiData[id][v].n.size > 0 || megamiData[id][v].s.size > 0);
            }).sort((a, b) => {
                if (a === 'o') return -1;
                if (b === 'o') return 1;
                return a.localeCompare(b);
            }) : ['o'];

            for (const v of versions) {
                const vName = v === 'o' ? "オリジン" : v.replace('a', 'アナザー');
                out += `=== "${vName}"\n\n`;
                
                // Unified Grid for both Normal and Special
                out += `    <div class="megami-card-grid" markdown>\n\n`;
                
                // Normal Cards (1-7)
                for (let i = 1; i <= 7; i++) {
                    out += this.renderCard(id, v, 'n', i, name, megamiData, cardMap, "normal-card");
                }
                
                // Special Cards (1-4)
                for (let i = 1; i <= 4; i++) {
                    out += this.renderCard(id, v, 's', i, name, megamiData, cardMap, "special-card");
                }
                
                out += `    </div>\n\n`;
            }
            out += "\n";
        }

        FileSystemAdapter.writeFileSync(outputCardsPath, out);
        console.log(`Synced cards to ${outputCardsPath}`);
    }

    private renderCard(id: string, v: string, type: string, index: number, mName: string, data: any, cardMap: any, extraClass: string = ""): string {
        let versionsToTry = [v];
        if (v !== 'o') {
            versionsToTry.push('o');
        }

        let imgPath = "";
        let foundFilename = "";

        for (const ver of versionsToTry) {
            const filename = `na_${id}_${ver}_${type}_${index}.png`;
            if (data[id] && data[id][ver]) {
                for (const folder of data[id][ver].folders) {
                    const potential = path.join(DOCS_DIR, 'assets/images/card/cards', folder, filename);
                    if (FileSystemAdapter.exists(potential)) {
                        imgPath = `../assets/images/card/cards/${folder}/${filename}`;
                        foundFilename = filename;
                        break;
                    }
                }
            }
            if (imgPath) break;
        }

        if (!imgPath) {
            const filename = `na_${id}_${v}_${type}_${index}.png`;
            const folder = `na_${id}_${v}_${type}`;
            imgPath = `${this.config.urls.base_card_url}images/card/cards/${folder}/${filename}`;
            foundFilename = filename;
        }

        let anchor = "";
        const cardName = cardMap[foundFilename];
        if (cardName) {
            const cleanName = cardName.replace(/\[([^\]]+)\]\(.*?\)/g, '$1').trim();
            const safeName = cleanName.replace(/[(){}\[\]「」]/g, '').replace(/\s+/g, '_');
            anchor = ` id="${safeName}"`;
        }

        const isShared = !foundFilename.includes(`_${v}_`) && v !== 'o';
        const opacityClass = isShared ? ' shared-card' : '';
        const sharedLabel = isShared ? ' (共通)' : '';

        return `    -   <span${anchor}></span>[:external-link: ![${mName}${sharedLabel}](${imgPath})](${imgPath}){ .glightbox .card-img .${extraClass}${opacityClass} }\n\n`;
    }
}
