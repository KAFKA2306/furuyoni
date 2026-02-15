import fs from 'fs-extra';
import yaml from 'js-yaml';
import { Config } from '../domain/Config';
import { MappingService } from '../domain/MappingService';
import { DOCS_DIR, PROJECT_ROOT, BLACKLIST } from '../domain/Constants';
import { AddLinks } from '../usecases/AddLinks';
import { SyncCards } from '../usecases/SyncCards';
import { DownloadAssets } from '../usecases/DownloadAssets';
import { AddAnchors } from '../usecases/AddAnchors';
import { Audit } from '../usecases/Audit';

export class ConfigLoader {
    static load(path: string): Config {
        const content = fs.readFileSync(path, 'utf8');
        return yaml.load(content) as Config;
    }
}
