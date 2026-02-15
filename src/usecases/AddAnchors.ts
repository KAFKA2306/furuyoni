import path from 'path';
import { FileSystemAdapter } from '../infrastructure/FileSystemAdapter';
import { DOCS_DIR } from '../domain/Constants';

export class AddAnchors {
    execute(): void {
        const cardFile = path.join(DOCS_DIR, 'megami/cards.md');
        if (!FileSystemAdapter.exists(cardFile)) {
            console.error(`Error: ${cardFile} not found.`);
            process.exit(1);
        }

        const content = FileSystemAdapter.readFileSync(cardFile);
        const lines = content.split('\n');
        const newLines: string[] = [];
        let updated = false;

        for (let i = 0; i < lines.length; i++) {
            const line = lines[i];
            const stripped = line.trim();

            // Heuristic: Card name line usually follows an image line
            if (i > 0) {
                const prevLine = lines[i - 1].trim();
                // Image line detection
                if (prevLine.startsWith('- ') && prevLine.includes('[:external-link:')) {
                    // Current line is the card name line if it's indented and text (not a list item itself)
                    if (line.startsWith('    ') && !stripped.startsWith('-') && stripped) {
                        // Check if already has anchor
                        if (stripped.includes('{: #')) {
                            newLines.push(line);
                            continue;
                        }

                        const baseText = stripped.split('{')[0].trim();
                        // Create anchor
                        const newLine = `    ${baseText} {: #${baseText} }`;
                        newLines.push(newLine);
                        updated = true;
                        continue;
                    }
                }
            }
            newLines.push(line);
        }

        if (updated) {
            FileSystemAdapter.writeFileSync(cardFile, newLines.join('\n'));
            console.log(`Updated ${cardFile} with anchors.`);
        } else {
            console.log("No new anchors needed.");
        }
    }
}
