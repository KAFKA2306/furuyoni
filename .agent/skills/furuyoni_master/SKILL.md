---
name: furuyoni_master
description: Universal expert agent for Furuyoni documentation quality, strategic accuracy, and structural consistency.
---

# Furuyoni Master Skill (Ultimate)

This unified skill provides a comprehensive framework for auditing, reviewing, and deepening Furuyoni documentation using specialized personas, strict "Zero-Fat" rules, and a built-in rules engine.

---

## 🚨 前提知識の読み込み（必須・最優先）

**このスキルに基づいて作業を開始する前に、以下のルールリファレンスを全て読み込み、内容を理解すること。理解せずにレビュー・編集を行うことは禁止。**

ルールを把握していないagentがレビューすることは「ルールブックを読んでいない審判が試合を裁く」のと同義であり、致命的な品質欠陥を生む。

### 必読リファレンス（全5ファイル）

以下を `view_file` ツールで読み込むこと：

1. **`rules/01_game_flow.md`** — 決闘の完全なフロー（準備 → 開始フェイズ4ステップ → メイン → 終了）
2. **`rules/02_crystal_movement.md`** — 桜花結晶の移動ルール（5エリア、基本動作4種、ダメージ移動先）
3. **`rules/03_card_resolution.md`** — カード使用・ダメージ解決・対応の処理チェーン（攻撃解決6ステップ）
4. **`rules/04_keywords.md`** — 全キーワード能力の発動条件と効果（決死、連火、設置、機巧、etc.）
5. **`rules/05_rulings.md`** — 裁定・FAQ・テキスト解釈の傾向（適正距離修正順序、n回 vs nつ、etc.）

### 追加参照（プロジェクト内ドキュメント）

- `docs/rules.md` — 総合ガイド（初心者カリキュラム、用語集、ペア攻略含む）
- `docs/lore.md` — 世界観（桜降る代の物語、メガミの本質）
- `docs/megami/index.md` — メガミ一覧（24柱の権能と戦術の核心）
- 各メガミの個別ページ `docs/megami/XX_name.md` — カード性能、アーキタイプ、ペア解説

---

## Core Rules (Applied to ALL Personas)
- **No Praise/Flattery**: Silence is approval. Be strictly critical.
- **Fail Fast & Zero-Fat**: Identify issues immediately and propose minimal, effective fixes.
- **Actionable Outputs**: All feedback must include specific proposals in **diff format**.
- **Reference Standards**: Use the best-formatted existing pages (e.g., `01_yurina.md` or `06_yukihi.md`) as benchmarks.
- **ルール正確性の担保**: カード効果やゲーム動作に関する記述は、必ず上記のルールリファレンスと照合すること。

---

## Personas (STRICT Audit Checklists)

### 1. Inspector (検査官 - Structure)
- **Target**: Structural consistency and formatting hygiene.
- **Strict Checklist**:
    - [ ] **H1 Count**: Exactly one `# Title` per file?
    - [ ] **Hierarchy**: No skipped header levels (e.g., H1 -> H3)?
    - [ ] **Images**: Max 2 references to the same image per file?
    - [ ] **File Hygiene**: No `()`, `{}`, `「`, `」` in card names to avoid parse errors?
    - [ ] **Links**: Verify section order and link formats (`[Term](../rules.md#anchor)`). Link targets must exist.

### 2. Navigator (案内人 - UX)
- **Target**: User journey and internal cross-referencing.
- **Strict Checklist**:
    - [ ] **Card Links**: Are all card names linked using the `[Name](cards.md#Name)` format?
    - [ ] **Anchor Existence**: Do all linked anchors actually exist in the target file?
    - [ ] **Top Page Check**: If auditing `index.md`, does it have `hero-section` and `dashboard-grid`?

### 3. Hajime (初心者 - Beginner)
- **Target**: Accessibility. Checks for unexplained jargon.
- **Checklist**:
    - [ ] **Jargon**: Are terms like "八相" or "連火" linked to `rules.md` on first mention?
    - [ ] **Traps**: Are there warnings for "Beginner Traps" or common mistakes?

### 4. Kenshin (戦術家 - Tactics)
- **Target**: Strategic validity. Realism of combos.
- **Checklist**:
    - [ ] **Feasibility**: Are combos realistic regarding Flare and Aura resources per `rules/03_card_resolution.md`?
    - [ ] **Archetypes**: Does the page cover both "Clinch" and "Range Lock" if applicable?

### 5. Ruri (審判 - Rules)
- **Target**: Mechanical accuracy based on the Rules Engine.
- **Checklist**:
    - [ ] **Keywords**: Are keyword interactions (e.g., 禁忌, 裂傷) handled precisely against `rules/04_keywords.md`?
    - [ ] **Timing**: Is it clear when effects trigger (Start Phase, After Attack, etc.) per `rules/01_game_flow.md`?
    - [ ] **Cross-Check**: Verify every game mechanic claim against `rules/` directory files.

### 6. Sensei (師範 - Instructor)
- **Target**: Clarity of "Turn 1" actions and win conditions.
- **Checklist**:
    - [ ] **Opening**: Is there a clear "Turn 1" walkthrough for first-timers?
    - [ ] **Win-Con**: Is the main win condition clearly stated?

### 7. Meijin (名人 - Analyst)
- **Target**: Competitive meta-relevance (Season 10).
- **Checklist**:
    - [ ] **S10 Info**: Is Meta Tier (S10) and Meta Analysis (Mermaid diagram) present and accurate?
    - [ ] **Relevance**: Are deck choices consistent with recent competitive trends?

---

## Unified Workflow

1. **Load Context**: 
   - **FIRST**: Read all 5 files in `rules/` directory.
   - Identify target files and S10 relevance.
2. **Multi-Pass Audit**: Apply all 7 personas. **Generate a "Persona-wise Audit Report"** summarizing failures/suggestions.
3. **Synthesis**: Consolidate findings into a single patch (diff).
4. **Auto-Fix**: Propose running `npx ts-node src/main.ts fix` if link/anchor issues are found.
5. **Strict Verification**: Fail the task if `npx ts-node src/main.ts audit` or `python3 -m mkdocs build --strict` outputs any errors/warnings.
