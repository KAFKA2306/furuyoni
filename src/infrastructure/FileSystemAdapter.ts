import fs from 'fs-extra';
import path from 'path';

export class FileSystemAdapter {
    static readFileSync(filePath: string): string {
        return fs.readFileSync(filePath, 'utf8');
    }

    static writeFileSync(filePath: string, content: string): void {
        fs.writeFileSync(filePath, content, 'utf8');
    }

    static exists(filePath: string): boolean {
        return fs.existsSync(filePath);
    }

    static ensureDir(dirPath: string): void {
        fs.ensureDirSync(dirPath);
    }

    static *walkSync(dir: string): Generator<string> {
        const files = fs.readdirSync(dir);
        for (const file of files) {
            const pathToFile = path.join(dir, file);
            const isDirectory = fs.statSync(pathToFile).isDirectory();
            if (isDirectory) {
                yield* FileSystemAdapter.walkSync(pathToFile);
            } else {
                yield pathToFile;
            }
        }
    }
}
