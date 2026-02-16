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
        const imageMap: { [file: string]: { [image: string]: number } } = {};
        let hasErrors = false;

        // 1. Collect Links & Check Headings & Track Image Usage
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

            // Track Image Usage
            const images = this.extractImages(content);
            if (images.length > 0) {
                imageMap[relPath] = {};
                images.forEach(img => {
                    imageMap[relPath][img] = (imageMap[relPath][img] || 0) + 1;
                });
            }
        }

        // 2. Validate Links & Images
        console.log(`Validating ${linksToValidate.size} unique references (links/images)...`);
        const results: { [url: string]: string } = {};

        // Validate in batches / parallel
        const linkArray = Array.from(linksToValidate);
        await Promise.all(linkArray.map(async url => {
            // Internal links check
            if (!url.startsWith('http')) {
                const [targetPath, anchor] = url.split('#');

                // If it's an empty link or just an anchor in the same file
                if (!targetPath && anchor) {
                    results[url] = "OK"; // Anchor in the same file is harder to verify without context, assuming OK for now or handled by individual file scan
                    return;
                }

                // Resolve path relative to DOCS_DIR or current file? 
                // Markdown links are usually relative to the file. 
                // But extractLinks just gives the raw string. 
                // To be precise, we need to know WHICH file it came from.
                // Let's refine extractLinks to return { file: string, url: string }.
                results[url] = "INTERNAL_PENDING";
                return;
            }

            const { status, code } = await NetworkAdapter.checkLink(url);
            results[url] = status === 'BROKEN' ? `BROKEN (${code})` : status;
        }));

        // Re-validate internal links with context
        for (const [file, links] of Object.entries(fileMap)) {
            const absoluteFilePath = path.join(PROJECT_ROOT, file);
            const currentDir = path.dirname(absoluteFilePath);

            for (const url of links) {
                if (url.startsWith('http')) {
                    const status = results[url];
                    if (status === 'OK') continue;
                    if (status === 'TIMEOUT' || status === 'CONNECTION_ERROR') {
                        console.warn(`  WARN: ${status} for ${url} in ${file}`);
                        continue;
                    }
                    console.error(`Broken link in ${file}: ${url} (${status})`);
                    hasErrors = true;
                    continue;
                }

                // Internal link validation
                const [relPath, anchor] = url.split('#');
                if (!relPath && anchor) continue; // Same-file anchor

                let targetAbsPath = path.resolve(currentDir, relPath);

                // If the link is to a directory, append index.md
                if (FileSystemAdapter.exists(targetAbsPath) && FileSystemAdapter.statSync(targetAbsPath).isDirectory()) {
                    targetAbsPath = path.join(targetAbsPath, 'index.md');
                }

                if (!FileSystemAdapter.exists(targetAbsPath)) {
                    console.error(`Broken internal link in ${file}: ${url} (File not found: ${path.relative(PROJECT_ROOT, targetAbsPath)})`);
                    hasErrors = true;
                    continue;
                }

                if (anchor) {
                    const targetContent = FileSystemAdapter.readFileSync(targetAbsPath);
                    // Simple check for anchor: either <a name="anchor">, <div id="anchor">, or # Heading
                    const anchorRegex = new RegExp(`(id|name)=["']${anchor}["']|#[#\s]*${anchor}`, 'i');
                    const slugifiedAnchor = anchor.toLowerCase().replace(/\s+/g, '-').replace(/[^\w-]/g, '');
                    const headingRegex = new RegExp(`^#+\\s+.*`, 'gm');

                    let found = anchorRegex.test(targetContent);
                    if (!found) {
                        // Check for slugified headings (common in mkdocs)
                        const headings = targetContent.match(headingRegex) || [];
                        found = headings.some(h => {
                            const hText = h.replace(/^#+\s+/, '').trim();
                            const hSlug = hText.toLowerCase().replace(/\s+/g, '-').replace(/[^\w-]/g, '');
                            return hSlug === slugifiedAnchor || hSlug === anchor;
                        });
                    }

                    if (!found) {
                        console.error(`Broken anchor in ${file}: ${url} (Anchor '${anchor}' not found in ${path.relative(PROJECT_ROOT, targetAbsPath)})`);
                        hasErrors = true;
                    }
                }
            }
        }

        if (hasErrors) {
            process.exit(1);
        }

        // 3. Check Image Duplication (STRICT)
        const MAX_IMAGE_REFERENCES = 2; // STRICT Rule: 3 or more = failure
        console.log("Checking for excessive image duplication...");
        for (const [file, images] of Object.entries(imageMap)) {
            for (const [image, count] of Object.entries(images)) {
                if (count > MAX_IMAGE_REFERENCES) {
                    console.error(`Excessive image duplication in ${file}: ${image} appears ${count} times (max: ${MAX_IMAGE_REFERENCES})`);
                    hasErrors = true;
                }
            }
        }

        if (hasErrors) {
            process.exit(1);
        }

        // 4. Specialized Audit for Top Page (index.md)
        const indexPath = path.join(DOCS_DIR, 'index.md');
        if (FileSystemAdapter.exists(indexPath)) {
            console.log("Auditing top page (index.md) specifically...");
            const indexContent = FileSystemAdapter.readFileSync(indexPath);

            // Checks for common hero section issues
            if (!indexContent.includes('hero-section')) {
                console.warn("  WARN: Top page missing 'hero-section' class.");
            }
            if (!indexContent.includes('dashboard-grid')) {
                console.warn("  WARN: Top page missing 'dashboard-grid' class.");
            }
        }

        // 5. Nav Audit
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
        // Standard Markdown links: [text](url)
        const markdownRegex = /\[.*?\]\((.*?)\)/g;
        // Image tags: ![alt](url)
        const imageRegex = /!\[.*?\]\((.*?)\)/g;
        // HTML img tags: <img ... src="url" ...>
        const htmlImgRegex = /<img\s+[^>]*src=["'](.*?)["'][^>]*>/g;
        // HTML anchor tags: <a ... href="url" ...>
        const htmlAnchorRegex = /<a\s+[^>]*href=["'](.*?)["'][^>]*>/g;

        let match;
        while ((match = markdownRegex.exec(content)) !== null) links.push(match[1]);
        while ((match = imageRegex.exec(content)) !== null) links.push(match[1]);
        while ((match = htmlImgRegex.exec(content)) !== null) links.push(match[1]);
        while ((match = htmlAnchorRegex.exec(content)) !== null) links.push(match[1]);

        return Array.from(new Set(links.filter(l => l && !l.startsWith('#'))));
    }

    private extractImages(content: string): string[] {
        const images: string[] = [];
        // Image tags: ![alt](url)
        const imageRegex = /!\[.*?\]\((.*?)\)/g;
        // HTML img tags: <img ... src="url" ...>
        const htmlImgRegex = /<img\s+[^>]*src=["'](.*?)["'][^>]*>/g;

        let match;
        while ((match = imageRegex.exec(content)) !== null) {
            const imagePath = match[1].split(')')[0]; // Remove any trailing attributes like { .glightbox }
            images.push(imagePath);
        }
        while ((match = htmlImgRegex.exec(content)) !== null) images.push(match[1]);

        // Extract only the filename for comparison (ignore path differences)
        return images.map(img => {
            const filename = img.split('/').pop() || img;
            return filename.split('?')[0]; // Remove query params if any
        }).filter(f => f && f.endsWith('.png'));
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
