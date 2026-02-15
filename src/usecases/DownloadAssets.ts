import path from 'path';
import { NetworkAdapter } from '../infrastructure/NetworkAdapter';
import { FileSystemAdapter } from '../infrastructure/FileSystemAdapter';
import { DOCS_DIR } from '../domain/Constants';

export class DownloadAssets {
    async execute(): Promise<void> {
        const dest = path.join(DOCS_DIR, 'assets/images');
        FileSystemAdapter.ensureDir(dest);

        const pat = /https:\/\/main-bakafire\.ssl-lolipop\.jp\/furuyoni\/na\/images\/([^\s\)"']+)/g;

        for (const file of FileSystemAdapter.walkSync(DOCS_DIR)) {
            if (!file.endsWith('.md')) continue;

            const content = FileSystemAdapter.readFileSync(file);
            const matches = Array.from(content.matchAll(pat));
            const uniqueImages = new Set(matches.map(m => m[1]));

            if (uniqueImages.size === 0) continue;

            for (const imgName of uniqueImages) {
                const localPath = path.join(dest, imgName);

                // Zero-Fat: Always download as per python script decision
                // "I will follow strictly: ALWAYS DOWNLOAD."
                try {
                    await NetworkAdapter.downloadFile(
                        `https://main-bakafire.ssl-lolipop.jp/furuyoni/na/images/${imgName}`,
                        localPath
                    );
                } catch (e) {
                    console.error(`Failed to download ${imgName}:`, e);
                }
            }

            const relPath = path.relative(path.dirname(file), dest);
            const newContent = content.replace(pat, (match: string, p1: string) => {
                return `${relPath}/${p1}`;
            });

            FileSystemAdapter.writeFileSync(file, newContent);
        }
        console.log("Assets downloaded and links updated.");
    }
}
