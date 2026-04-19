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
        out += "各メガミのタブから通常札と切札を確認できます。アナザー版ではオリジンと共通のカードは少し薄く表示されています。\n\n";

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

            // Only include versions that actually have at least one unique card locally, OR 'o'
            const versions = megamiData[id] ? Object.keys(megamiData[id]).filter(v => {
                if (v === 'o') return true;
                // Check if this version has any unique cards
                return (megamiData[id][v].n.size > 0 || megamiData[id][v].s.size > 0);
            }).sort((a, b) => {
                if (a === 'o') return -1;
                if (b === 'o') return 1;
                return a.localeCompare(b);
            }) : ['o'];

            for (const v of versions) {
                const vName = v === 'o' ? "オリジン" : v.replace('a', 'アナザー');
                out += `=== "${vName}"\n\n`;
                
                out += `    ### 通常札\n\n    <div class="grid cards" markdown>\n\n`;
                for (let i = 1; i <= 7; i++) {
                    out += this.renderCard(id, v, 'n', i, name, megamiData, cardMap);
                }
                out += `    </div>\n\n`;

                out += `    ### 切札\n\n    <div class="grid cards special-cards" markdown>\n\n`;
                for (let i = 1; i <= 4; i++) {
                    out += this.renderCard(id, v, 's', i, name, megamiData, cardMap);
                }
                out += `    </div>\n\n`;
            }
            out += "\n";
        }

        FileSystemAdapter.writeFileSync(outputCardsPath, out);
        console.log(`Synced cards to ${outputCardsPath}`);
    }

    private renderCard(id: string, v: string, type: string, index: number, mName: string, data: any, cardMap: any): string {
        let versionsToTry = [v];
        if (v !== 'o') {
            versionsToTry.push('o'); // Fallback to Origin if Another card doesn't exist (shared cards)
        }

        let imgPath = "";
        let foundFilename = "";

        for (const ver of versionsToTry) {
            const filename = `na_${id}_${ver}_${type}_${index}.png`;
            
            // Find local path if exists
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

        // If still not found locally, try to guess official URL for the REQUESTED version
        if (!imgPath) {
            const filename = `na_${id}_${v}_${type}_${index}.png`;
            const folder = `na_${id}_${v}_${type}`;
            imgPath = `${this.config.urls.base_card_url}images/card/cards/${folder}/${filename}`;
            foundFilename = filename;
            
            // Note: We don't fallback to official Origin URL here because 
            // if we don't have it locally, we probably don't need it or it's genuinely missing.
            // But actually, for standard Origin cards, we should probably include them.
            if (v === 'o') {
                // Keep it, DownloadAssets will try to get it.
            } else {
                // For Another cards that don't exist locally, we might be guessing wrong.
                // However, many Another cards ARE replacements.
                // Let's only include it if it's likely to exist or if it's Origin.
                // For now, let's just include it and let DownloadAssets/Audit handle it.
            }
        }

        let anchor = "";
        const cardName = cardMap[foundFilename];
        if (cardName) {
            const cleanName = cardName.replace(/\[([^\]]+)\]\(.*?\)/g, '$1').trim();
            const safeName = cleanName.replace(/[(){}\[\]「」]/g, '').replace(/\s+/g, '_');
            anchor = ` id="${safeName}"`;
        }

        // Visual indicator for shared cards
        const isShared = !foundFilename.includes(`_${v}_`) && v !== 'o';
        const opacityStyle = isShared ? ' style="opacity: 0.8; filter: grayscale(20%);"' : '';
        const sharedLabel = isShared ? ' (共通)' : '';

        return `    -   <span${anchor}></span>[:external-link: ![${mName}${sharedLabel}](${imgPath})](${imgPath}){ .glightbox ${opacityStyle} }\n\n`;
    }
}
