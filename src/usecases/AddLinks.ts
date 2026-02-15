import path from 'path';
import { Config } from '../domain/Config';
import { FileSystemAdapter } from '../infrastructure/FileSystemAdapter';
import { MappingService } from '../domain/MappingService';
import { DOCS_DIR } from '../domain/Constants';

export class AddLinks {
    constructor(private config: Config) { }

    execute(): void {
        const staticMapping = this.config.term_mapping || {};
        const cardMap = MappingService.extractCardMappingFromCardsFile();
        const megamiMap = MappingService.extractMegamiMapping();

        const allTerms = [
            ...Object.keys(staticMapping),
            ...Object.keys(cardMap),
            ...Object.keys(megamiMap)
        ].sort((a, b) => b.length - a.length);

        if (allTerms.length === 0) {
            console.log("No terms to link.");
            return;
        }

        // JS Regex for skip pattern
        const skipPattern = /(```[\s\S]*?```|\[[^\]]*?\]\([^\)]*?\)|!\[.*?\]\(.*?\)|`[^`\n]+`|<[^>]+>)/g;

        // We can't easily combine skip and terms into one regex if terms are too many or complex chars.
        // But let's try strict replication of python logic.
        const termRegexStr = allTerms.map(t => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|');
        const masterPattern = new RegExp(`(${skipPattern.source})|(${termRegexStr})`, 'gm');

        for (const file of FileSystemAdapter.walkSync(DOCS_DIR)) {
            if (!file.endsWith('.md')) continue;

            const content = FileSystemAdapter.readFileSync(file);
            let newContent = content.replace(masterPattern, (match: string, skipped: string | undefined, term: string | undefined) => {
                if (skipped) {
                    // Python logic: check if it's a link we should update [Term](Url)
                    const linkMatch = skipped.match(/^\[([^\]]+)\]\(([^\)]+)\)$/);
                    if (linkMatch) {
                        const linkTerm = linkMatch[1];
                        if (cardMap[linkTerm] || megamiMap[linkTerm] || staticMapping[linkTerm]) {
                            // Valid term inside a link, but is it the right link? 
                            // Python logic says: "Fall through to re-generate link" -> meaning return null?
                            // No, python logic: if skipped matches (group 1), it enters:
                            //   if match.group(1):
                            //      if link_match: ... pass (meaning loop continues to next check? no `pass` in python just does nothing)
                            //      else: return match.group(1)
                            //   
                            // Wait, if `pass`, it falls down to `if term in card_map...`.
                            // So if it IS a link [Term](OldUrl) and Term is in our map, we might want to update it.
                            // But `replace` in JS works differently.
                            // We need to decide what to return.

                            // Let's simplify: if it's a link [Term](...), should we update it?
                            // The python code updated it if it matched a term we know.
                            // So we treat `linkTerm` as the `term` to process.
                            term = linkTerm;
                            // And checking skipping logic again? Python:
                            /*
                            if skip_pattern.match(term) and not (match.group(1) and link_match):
                                return term
                            */
                            // If we already established it's a link_match, we proceed.
                        } else {
                            return skipped;
                        }
                    } else {
                        return skipped;
                    }
                }

                // It's a term (either from group 2 OR extracted from group 1 link)
                if (!term) return match; // Should not happen if logic is correct

                if (cardMap[term]) {
                    const url = cardMap[term];
                    return `[![${term}](${url})](${url}){ .glightbox }`;
                }

                let target: string | null = null;
                if (megamiMap[term]) {
                    target = megamiMap[term];
                } else if (staticMapping[term]) {
                    target = staticMapping[term];
                }

                if (target) {
                    // Check if self-link
                    let targetFile = target;
                    let anchorPart = "";
                    if (target.includes('#')) {
                        const parts = target.split('#');
                        targetFile = parts[0];
                        anchorPart = '#' + parts[1];
                    }

                    const targetAbs = path.resolve(DOCS_DIR, targetFile);
                    const currentAbs = path.resolve(file);

                    if (targetAbs === currentAbs) {
                        if (anchorPart) {
                            return `[${term}](${anchorPart})`;
                        }
                        return term; // Don't link to self if no anchor
                    }

                    const relPath = path.relative(path.dirname(file), path.join(DOCS_DIR, targetFile));
                    return `[${term}](${relPath}${anchorPart})`;
                }

                return term;
            });

            if (newContent !== content) {
                FileSystemAdapter.writeFileSync(file, newContent);
                // console.log(`Linked ${file}`);
            }
        }
        console.log("Added links to markdown files.");
    }
}
