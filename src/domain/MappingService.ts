import path from 'path';
import { FileSystemAdapter } from '../infrastructure/FileSystemAdapter';
import { DOCS_DIR, BLACKLIST } from './Constants';

export class MappingService {
    static extractMegamiMapping(): { [key: string]: string } {
        const mapping: { [key: string]: string } = {};
        const indexFile = path.join(DOCS_DIR, 'megami/index.md');

        if (!FileSystemAdapter.exists(indexFile)) return mapping;

        const content = FileSystemAdapter.readFileSync(indexFile);
        const pattern = /\[([^\]]+)\]\(([^)]+\.md)\)/g;

        let match;
        while ((match = pattern.exec(content)) !== null) {
            const name = match[1];
            const filePath = match[2];
            // Filter for expected megami files (01-16, index, cards)
            // Python regex: ^(0[1-9]|1[0-6]|index|cards)
            // Let's be slightly more lenient or strict as needed.
            // Using the same regex logic.
            if (/^(0[1-9]|1[0-9]|2[0-9]|index|cards)/.test(filePath)) {
                mapping[name] = `megami/${filePath}`;
            }
        }
        return mapping;
    }

    static buildCardMap(docsRoot: string = DOCS_DIR): { [filename: string]: string } {
        const cardMap: { [filename: string]: string } = {};
        // Relaxed header pattern to catch formats like "### [N1 Name](...)" or "### N1 Name"
        const headerPat = /^#{3,4}\s+(?:\[?(?:[NS]10|[NS]\d+|[A-Z]\d+)\s+)?([^\]\n]+)\]?(?:\(.*\))?$/gm;
        const tableRowPat = /^\s*\|\s*(?:\[?\*\*([^\]\*]+)\*\*\]?\(.*?\)|([^\|]+))\s*\|/gm;
        const imgPat = /!\[([^\]]*)\]\((?:[^)]*\/)?([^/]+\.png)(?:\s.*?)?\)/g;

        const megamiDir = path.join(docsRoot, 'megami');
        if (!FileSystemAdapter.exists(megamiDir)) return cardMap;

        for (const file of FileSystemAdapter.walkSync(megamiDir)) {
            if (!file.endsWith('.md') || file.endsWith('cards.md') || file.endsWith('index.md')) continue;

            const content = FileSystemAdapter.readFileSync(file);
            const validNames = new Set<string>();

            // 1. Extract from headers and table rows using a more robust name-finding regex
            // This regex looks for [**Name**] or [Name](...) or just **Name**
            const nameExtractPat = /\[(?:\*\*)?([^\]\*]+)(?:\*\*)?\](?:\(.*\))?|\*\*([^\|\*]+)\*\*/g;

            let headerMatch;
            while ((headerMatch = headerPat.exec(content)) !== null) {
                const rawLine = headerMatch[0];
                let nameMatch;
                while ((nameMatch = nameExtractPat.exec(rawLine)) !== null) {
                    let candidate = (nameMatch[1] || nameMatch[2]).trim();
                    candidate = candidate.replace(/^[NS]\d+\s+/, '').trim();
                    if (candidate && !BLACKLIST.has(candidate) && candidate.length > 1) {
                        validNames.add(candidate.replace(/\[\*\*|\*\*\]/g, '').trim());
                    }
                }
            }

            headerPat.lastIndex = 0; // Reset
            let tableMatch;
            while ((tableMatch = tableRowPat.exec(content)) !== null) {
                const rawLine = tableMatch[0];
                let nameMatch;
                while ((nameMatch = nameExtractPat.exec(rawLine)) !== null) {
                    let candidate = (nameMatch[1] || nameMatch[2]).trim();
                    candidate = candidate.replace(/^[NS]\d+\s+/, '').trim();
                    if (candidate && !BLACKLIST.has(candidate) && candidate.length > 1 && !candidate.includes(':') && !candidate.includes('|')) {
                        validNames.add(candidate.replace(/\[\*\*|\*\*\]/g, '').trim());
                    }
                }
            }

            // 3. Map images to names
            let imgMatch;
            while ((imgMatch = imgPat.exec(content)) !== null) {
                const altText = imgMatch[1].trim();
                const filename = imgMatch[2].trim();

                if (validNames.has(altText)) {
                    cardMap[filename] = altText;
                }
            }
        }

        return cardMap;
    }

    static extractCardMappingFromCardsFile(): { [name: string]: string } {
        const mapping: { [name: string]: string } = {};
        const cardFile = path.join(DOCS_DIR, 'megami/cards.md');
        if (!FileSystemAdapter.exists(cardFile)) return mapping;

        const content = FileSystemAdapter.readFileSync(cardFile);
        // Pattern: <span id="CardName"></span>[:external-link: ![MegamiName](ImageURL)](ImageURL)
        const pattern = /<span id="([^"]+)"><\/span>\[:external-link: !\[[^\]]+\]\(([^)]+)\)\]\(([^)]+)\)/g;

        let match;
        while ((match = pattern.exec(content)) !== null) {
            const name = match[1];
            const url = match[2]; // Using image URL as the value, consistent with python
            mapping[name] = url;
        }
        return mapping;
    }
}
