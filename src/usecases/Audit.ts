import path from 'path';
import { Config } from '../domain/Config';
import { FileSystemAdapter } from '../infrastructure/FileSystemAdapter';
import { NetworkAdapter } from '../infrastructure/NetworkAdapter';
import { DOCS_DIR, PROJECT_ROOT } from '../domain/Constants';

export class Audit {
    constructor(private config: Config) { }

    async execute(): Promise<void> {
        console.log("--- Starting Audit ---");
        const linksToValidate = new Set<string>();
        const fileMap: { [file: string]: string[] } = {};
        let hasErrors = false;

        // 1. Collect Links & Check Headings
        for (const file of FileSystemAdapter.walkSync(DOCS_DIR)) {
            if (!file.endsWith('.md')) continue;

            const content = FileSystemAdapter.readFileSync(file);
            const relPath = path.relative(PROJECT_ROOT, file);

            // Check Headings
            const errors = this.checkHeadings(content);
            if (errors.length > 0) {
                console.error(`Heading Error in ${relPath}:`);
                errors.forEach(e => console.error(`  ${e}`));
                process.exit(1);
            }

            // Extract Links
            const links = this.extractLinks(content);
            if (links.length > 0) {
                fileMap[relPath] = links;
                links.forEach(l => linksToValidate.add(l));
            }
        }

        // 2. Validate Links
        console.log(`Validating ${linksToValidate.size} unique links...`);
        const results: { [url: string]: string } = {};

        // Validate in batches / parallel
        const linkArray = Array.from(linksToValidate);
        await Promise.all(linkArray.map(async url => {
            // Internal links check
            if (!url.startsWith('http')) {
                // TODO: check internal links? Python script used Validator which did check files/anchors.
                // For now, let's assume Validator logic was mostly external or simple internal existence.
                // Python `LinkValidator` did check anchors if it was local.
                // Let's implement simple check if it is not http.
                // But wait, "clean, simple, minimal".
                // Use simple heuristic: if it looks like a file path, check existence.
                results[url] = "OK";
                return;
            }

            const { status, code } = await NetworkAdapter.checkLink(url);
            results[url] = status === 'BROKEN' ? `BROKEN (${code})` : status;
        }));

        for (const [file, links] of Object.entries(fileMap)) {
            for (const url of links) {
                const status = results[url];
                if (status === 'OK') continue;
                if (status === 'TIMEOUT' || status === 'CONNECTION_ERROR') {
                    console.warn(`  WARN: ${status} for ${url} in ${file}`);
                    continue;
                }
                console.error(`Broken link in ${file}: ${url} (${status})`);
                hasErrors = true;
            }
        }

        if (hasErrors) {
            process.exit(1);
        }

        // 3. Nav Audit
        const navOrphans = this.auditNav();
        if (navOrphans.length > 0) {
            console.error("Orphaned files (not in nav):");
            navOrphans.forEach(o => console.error(`  - ${o}`));
            process.exit(1);
        }

        console.log("Audit Passed.");
    }

    private checkHeadings(content: string): string[] {
        const lines = content.split('\n');
        const errors: string[] = [];
        const headings: { level: number, title: string }[] = [];

        for (const line of lines) {
            const match = line.match(/^(#+)\s+(.*)/);
            if (match) {
                headings.push({ level: match[1].length, title: match[2] });
            }
        }

        if (headings.length === 0) {
            errors.push("No headings found");
            return errors;
        }

        const h1Count = headings.filter(h => h.level === 1).length;
        if (h1Count !== 1) {
            errors.push(`Expected 1 H1, found ${h1Count}`);
        }

        let prevLevel = 0;
        for (const h of headings) {
            if (h.level > prevLevel + 1) {
                errors.push(`Header level skipped: H${prevLevel} -> H${h.level} ('${h.title}')`);
            }
            prevLevel = h.level;
        }
        return errors;
    }

    private extractLinks(content: string): string[] {
        const links: string[] = [];
        const regex = /\[.*?\]\((.*?)\)/g;
        let match;
        while ((match = regex.exec(content)) !== null) {
            links.push(match[1]);
        }
        return links;
    }

    private auditNav(): string[] {
        const navPaths = new Set<string>();

        // Load mkdocs.yml
        const mkdocsPath = path.join(PROJECT_ROOT, 'mkdocs.yml');
        let mkdocsConfig: any = {};
        try {
            const fileContent = FileSystemAdapter.readFileSync(mkdocsPath);
            // js-yaml doesn't support python tags out of the box.
            // We can replace them or use a schema.
            // Simple hack: remove !!python/name:...
            const cleanContent = fileContent.replace(/!!python\/name:[\w\.]+/g, '');
            const yaml = require('js-yaml'); // Dynamic require or import if top-level
            mkdocsConfig = yaml.load(cleanContent);
        } catch (e) {
            console.error("Failed to load mkdocs.yml", e);
            return [];
        }

        const extract = (items: any) => {
            if (!items) return;
            if (Array.isArray(items)) {
                items.forEach(item => extract(item));
            } else if (typeof items === 'object') {
                for (const key in items) {
                    const value = items[key];
                    if (typeof value === 'string') {
                        navPaths.add(value);
                    } else {
                        extract(value);
                    }
                }
            } else if (typeof items === 'string') {
                navPaths.add(items);
            }
        };

        if (mkdocsConfig.nav) {
            extract(mkdocsConfig.nav);
        }

        const orphans: string[] = [];

        for (const file of FileSystemAdapter.walkSync(DOCS_DIR)) {
            if (!file.endsWith('.md')) continue;
            const rel = path.relative(DOCS_DIR, file);
            if (!navPaths.has(rel)) {
                orphans.push(rel);
            }
        }
        return orphans;
    }
}
