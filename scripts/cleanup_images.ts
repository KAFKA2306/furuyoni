import fs from 'fs';
import path from 'path';

const DOCS_DIR = 'docs/megami';

const cleanFile = (filePath: string) => {
    let content = fs.readFileSync(filePath, 'utf-8');

    // Pattern to match [![CardName](../assets/.../card_id.png)](../assets/...) { .glightbox }
    // and replace it with just CardName
    const regex = /\[\!\[([^\]]+)\]\(\.\.\/assets\/images\/card\/cards\/[^\)]+\)\]\(\.\.\/assets\/images\/card\/cards\/[^\)]+\)\{ [^\}]+\}/g;

    // Also handle simple [![CardName](path)](path) without glightbox
    const regexSimple = /\[\!\[([^\]]+)\]\(\.\.\/assets\/images\/card\/cards\/[^\)]+\)\]\(\.\.\/assets\/images\/card\/cards\/[^\)]+\)/g;

    const newContent = content.replace(regex, '$1').replace(regexSimple, '$1');

    if (content !== newContent) {
        fs.writeFileSync(filePath, newContent);
        console.log(`Cleaned: ${filePath}`);
    }
};

const main = () => {
    const files = fs.readdirSync(DOCS_DIR);
    files.forEach(file => {
        if (file.endsWith('.md') && file !== 'cards.md' && file !== 'index.md') {
            cleanFile(path.join(DOCS_DIR, file));
        }
    });

    // Also clean history files mentioned in audit
    const historyDir = 'docs/history';
    if (fs.existsSync(historyDir)) {
        const historyFiles = fs.readdirSync(historyDir);
        historyFiles.forEach(file => {
            if (file.endsWith('.md')) {
                cleanFile(path.join(historyDir, file));
            }
        });
    }
};

main();
