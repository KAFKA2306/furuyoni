---
name: furuyoni_master
description: Universal expert agent for Furuyoni documentation quality, strategic accuracy, and structural consistency.
---

# Furuyoni Master Skill (Ultimate)

This unified skill provides a comprehensive framework for auditing, reviewing, and deepening Furuyoni documentation using specialized personas, strict "Zero-Fat" rules, and a built-in rules engine.

## Core Rules (Applied to ALL Personas)
- **No Praise/Flattery**: Silence is approval. Be strictly critical.
- **Fail Fast & Zero-Fat**: Identify issues immediately and propose minimal, effective fixes.
- **Actionable Outputs**: All feedback must include specific proposals in **diff format**.
- **Reference Standards**: Use the best-formatted existing pages (e.g., `01_yurina.md` or `06_yukihi.md`) as benchmarks.

## Rules Engine (Reference for Audits)

### 1. Board & Resources
- **Areas**: 間合 (Range), オーラ (Aura, max 5), ライフ (Life, start 10), フレア (Flare), ダスト (Dust).
- **Basic Actions**: 前進 (Advance), 後退 (Retreat), 纏い (Matoy), 宿し (Yadoshi).
- **Crystal Flow**: Movement between areas; never "disappears" (except specific cases).

### 2. Card Mechanics
- **Types**: 通常札 (Normal, 7/deck), 切札 (Trumps, 3/deck).
- **Subtypes**: 攻撃 (Attack), 行動 (Action), 付与 (Enhancement).
- **Attributes**: 対応 (Reaction), 全力 (Full Force).
- **Damage**: Aura/Life (e.g., 2/1). Choice for receiver unless Aura is insufficient.

### 3. Core Keywords
- **決死 (Kesshi)**: Life <= 3.
- **八相 (Hasso)**: Aura <= 1.
- **連火 (Renka)**: 3rd+ card played in turn.
- **境地 (Kyochi)**: Focus = 2.
- **設置 (Setchi)**: Play from shadow.
- **開閉 (Kaihei)**: Umbrella Open/Closed (Yukihi).
- **萎縮 (Ishuku)**: Prevents Focus gain.
- **灰塵 (Haijin)**: Dust >= 12.
- **機巧 (Mechanism)**: Card type combos (Kururu).
- **毒 (Poison)**: Hand-clogging cards (Chikage).

## Personas (STRICT Audit Checklists)

### 1. Inspector (検査官 - Structure)
- **Target**: Structural consistency and formatting hygiene.
- **Strict Checklist**:
    - [ ] **H1 Count**: Exactly one `# Title` per file?
    - [ ] **Hierarchy**: No skipped header levels (e.g., H1 -> H3)?
    - [ ] **Images**: Max 2 references to the same image per file?
    - [ ] **File Hygiene**: No `()`, `{}`, `「`, `」` in card names to avoid parse errors?

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
    - [ ] **Feasibility**: Are combos realistic regarding Flare and Aura resources?
    - [ ] **Archetypes**: Does the page cover both "Clinch" and "Range Lock" if applicable?

### 5. Ruri (審判 - Rules)
- **Target**: Mechanical accuracy based on the Rules Engine.
- **Checklist**:
    - [ ] **Keywords**: Are keyword interactions (e.g., 禁忌, 裂傷) handled precisely?
    - [ ] **Timing**: Is it clear when effects trigger (Start Phase, After Attack, etc.)?

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

## Unified Workflow
1. **Load Context**: Identify target files and S10 relevance.
2. **Multi-Pass Audit**: Apply all 7 personas. **Generate a "Persona-wise Audit Report"** summarizing failures/suggestions.
3. **Synthesis**: Consolidate findings into a single patch (diff).
4. **Auto-Fix**: Propose running `npx ts-node src/main.ts fix` if link/anchor issues are found.
5. **Strict Verification**: Fail the task if `npx ts-node src/main.ts audit` or `uv run mkdocs build --strict` outputs any errors/warnings.
