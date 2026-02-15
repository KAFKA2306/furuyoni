import axios from 'axios';
import fs from 'fs-extra';
import path from 'path';

export class NetworkAdapter {
    static async downloadFile(url: string, destPath: string): Promise<void> {
        const response = await axios({
            method: 'GET',
            url: url,
            responseType: 'stream',
            headers: { 'User-Agent': 'Mozilla/5.0' }
        });

        await fs.ensureDir(path.dirname(destPath));
        const writer = fs.createWriteStream(destPath);
        response.data.pipe(writer);

        return new Promise((resolve, reject) => {
            writer.on('finish', resolve);
            writer.on('error', reject);
        });
    }

    static async checkLink(url: string): Promise<{ status: string; code?: number }> {
        try {
            const response = await axios.head(url, { timeout: 5000, headers: { 'User-Agent': 'Mozilla/5.0' } });
            return { status: 'OK', code: response.status };
        } catch (error: any) {
            if (error.code === 'ECONNABORTED') return { status: 'TIMEOUT' };
            if (error.response) return { status: 'BROKEN', code: error.response.status };
            return { status: 'CONNECTION_ERROR' };
        }
    }
}
