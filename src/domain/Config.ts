export interface Config {
    model: string;
    paths: {
        data_js: string;
        output_cards: string;
        [key: string]: string;
    };
    urls: {
        base_card_url: string;
        [key: string]: string;
    };
    term_mapping: {
        [key: string]: string;
    };
    nav?: Array<string | { [key: string]: string | Array<string | { [key: string]: string }> }>;
}
