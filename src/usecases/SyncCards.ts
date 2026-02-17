import path from 'path';
import { Config } from '../domain/Config';
import { FileSystemAdapter } from '../infrastructure/FileSystemAdapter';
import { MappingService } from '../domain/MappingService';
import { PROJECT_ROOT } from '../domain/Constants';

export class SyncCards {
    constructor(private config: Config) { }

    execute(): void {
        const dataJsPath = path.join(PROJECT_ROOT, this.config.paths.data_js);
        const outputCardsPath = path.join(PROJECT_ROOT, this.config.paths.output_cards);

        if (!FileSystemAdapter.exists(dataJsPath)) {
            console.error(`Error: ${dataJsPath} not found.`);
            return;
        }

        const cardMap = MappingService.buildCardMap();
        const megamiMap = MappingService.extractMegamiMapping();

        const content = FileSystemAdapter.readFileSync(dataJsPath);
        const startMarker = "export const cards = {";
        const sIdx = content.indexOf(startMarker);

        if (sIdx === -1) {
            console.error("Error: Could not find 'export const cards = {' in data.js");
            return;
        }

        // Simple heuristic to find the end of the object. 
        // Assuming it ends with "};" as per python script logic which looked for "};"
        const eIdx = content.indexOf("};", sIdx);
        if (eIdx === -1) {
            console.error("Error: Could not find end of cards object in data.js");
            return;
        }

        const raw = content.substring(sIdx + "export const cards = ".length, eIdx + 1).trim();
        // Convert JS object literal to JSON-like string (replace single quotes with double, fix keys etc)
        // Python: raw.strip().replace("'", '"')
        // And regex to fix trailing commas or unquoted keys if necessary.
        // JS object keys might, or might not be quoted.
        // `export const cards = { 'key': ['val'], ... }`

        // Let's try a safer evaluation or strict parsing if format is known.
        // Since we are shifting to TS, we can simply `require` or `import` the file if it was a module,
        // but it's a JS file in a potentially typescript project, and we want to read it as data.
        // Let's stick to the parsing logic if it works, or use eval/new Function (risky but easy for local script).

        let data: { [key: string]: string[] } = {};
        try {
            // Safe-ish eval for data file
            // Note: This assumes the file content is trusted (it is user code)
            const jsonStr = raw
                .replace(/'/g, '"') // replace single quotes
                .replace(/,\s*([\]}])/g, '$1'); // remove trailing commas
            data = JSON.parse(jsonStr);
        } catch (e) {
            console.error("Failed to parse data.js. Trying simple eval fallback.");
            try {
                // Determine strict subset?
                // fallback to python logic simulation:
                // It just did replace "'" -> '"' and regex sub to remove trailing commas.
                const jsonStr = raw
                    .replace(/'/g, '"') // replace single quotes
                    .replace(/,\s*([\]}])/g, '$1'); // remove trailing commas
                data = JSON.parse(jsonStr);
            } catch (e2) {
                console.error("Parsing failed.", e2);
                return;
            }
        }

        let out = "# 全カード一覧\n\n";

        for (const [m, ps] of Object.entries(data)) {
            let headerAttr = "";
            if (megamiMap[m]) {
                const fname = path.basename(megamiMap[m]);
                const match = fname.match(/\d+_(\w+)\.md/);
                if (match) {
                    headerAttr = ` {: #${match[1]} }`;
                }
            }

            out += `## ${m}${headerAttr}\n\n<div class="grid cards" markdown>\n\n`;

            for (const p of ps) {
                const url = `${this.config.urls.base_card_url}${p}`;
                const filename = path.basename(p);
                let anchor = "";

                if (cardMap[filename]) {
                    // Clean name: remove links if any (though mapped value should be clean)
                    const cleanName = cardMap[filename].replace(/\[([^\]]+)\]\(.*?\)/g, '$1').trim();
                    // Remove characters that break anchor parsing: (), {}, [], 「」
                    // And replace spaces with underscores for ID compatibility with links
                    const safeName = cleanName.replace(/[(){}\[\]「」]/g, '').replace(/\s+/g, '_');
                    anchor = ` id="${safeName}"`;
                }

                if (anchor) {
                    out += `-   <span${anchor}></span>[:external-link: ![${m}](${url})](${url}){ .glightbox }\n\n`;
                } else {
                    out += `-   [:external-link: ![${m}](${url})](${url}){ .glightbox }\n\n`;
                }
            }
            out += "</div>\n\n";
        }

        FileSystemAdapter.writeFileSync(outputCardsPath, out);
        console.log(`Synced cards to ${outputCardsPath}`);
    }
}
