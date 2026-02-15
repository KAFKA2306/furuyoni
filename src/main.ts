#!/usr/bin/env node
import { Command } from 'commander';
import path from 'path';
import { ConfigLoader } from './infrastructure/ConfigLoader';
import { AddLinks } from './usecases/AddLinks';
import { SyncCards } from './usecases/SyncCards';
import { DownloadAssets } from './usecases/DownloadAssets';
import { AddAnchors } from './usecases/AddAnchors';
import { Audit } from './usecases/Audit';
import { PROJECT_ROOT } from './domain/Constants';

async function main() {
    const program = new Command();
    const configPath = path.join(PROJECT_ROOT, 'config.yaml');
    const config = ConfigLoader.load(configPath);

    program
        .name('maintain')
        .description('Maintenance scripts for Furuyoni documentation');

    program.command('fix')
        .description('Run all destructive fixes (links, cards, assets, anchors)')
        .action(async () => {
            console.log("--- Running All Fixes ---");
            new AddLinks(config).execute();
            new SyncCards(config).execute();
            await new DownloadAssets().execute();
            new AddAnchors().execute();
            console.log("--- All Fixes Completed ---");
        });

    program.command('add-links').action(() => new AddLinks(config).execute());
    program.command('sync-cards').action(() => new SyncCards(config).execute());
    program.command('download-assets').action(async () => await new DownloadAssets().execute());
    program.command('add-anchors').action(() => new AddAnchors().execute());
    program.command('audit').action(async () => await new Audit(config).execute());

    program.parse(process.argv);
}

main();
