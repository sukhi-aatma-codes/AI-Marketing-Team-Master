# Custom Skill Integration & Execution Guidelines

**Version:** 1.0  
**Audience:** Developers & Agent Engineers  
**Location:** `.claude\skills\`  

This document outlines the strict guidelines and contracts that all custom developer skills in this workspace must follow. Adhering to these rules ensures that skills remain modular, reusable, robust, and highly predictable for downstream sub-agents and orchestrators.

---

## 1. Core Principles

1. **Strict Brand Agnosticism:**
   * **Rule:** Never hardcode client-specific variables (company names, service names, hex colors, font types, logos, target URLs, domain credentials, key focus terms) inside a skill's scripts or configuration.
   * **Alternative:** Pass these parameters dynamically during skill execution, or write the skill to query and parse the relevant file under `_context\` at runtime.

2. **Standardized Parameter Schema:**
   * Every skill's runner script must accept parameters via standardized environment variables, JSON config files, or standard CLI arguments.
   * Example CLI parameter pattern:
     ```bash
     python .claude/skills/my-skill/run.py --brand-context "./_context/Brand_Context.md" --output-dir "./reports/"
     ```

3. **Deterministic Output Contracts:**
   * All skills must produce standardized, predictable output formats so that sub-agents and automated pipelines can easily verify execution success.
   * Every execution must output a **standard JSON summary file** named `execution-summary.json` in the target output directory detailing:
     ```json
     {
       "skillName": "blog-writer",
       "timestamp": "2026-05-25T14:25:00Z",
       "success": true,
       "generatedFiles": [
         "output/pages/blog-ai-ops-2026-05-25.md",
         "output/pages/blog-ai-ops-2026-05-25.html"
       ],
       "metrics": {
         "wordCount": 1240,
         "readabilityScore": 68.2
       }
     }
     ```

4. **Editorial Integrity (No AI Speak or Em Dashes):**
   * **Rule:** All skills generating editorial or copywriting output must avoid standard LLM structural artifacts, generic corporate buzzwords (*delve, leverage, robust, testaments, revolutionize, seamless*), and ban the use of em dashes (—) for dramatic transitions (use commas, colons, or parentheses instead) to keep outputs sounding completely human-authored.

---

## 2. Directory Structure for Skills

Each custom skill in the `.claude\skills\` folder must be self-contained:
```
.claude/skills/my-custom-skill/
├── SKILL_README.md       ← Comprehensive brief, requirements, parameters description
├── run.py / run.sh       ← Execution entry-point wrapper
├── src/                  ← Core implementation source code
└── templates/            ← Reusable layout/formatting blueprints (client-agnostic)
```

---

## 3. Sandboxed Output Mapping
All skills must route their final output strictly to the appropriate workspace folders as outlined in the global instructions:

| Skill Focus | Primary Target Folder |
|---|---|
| Ad copy, creative visuals, campaign media | `output\ads\` |
| Gated assets, checklists, whitepapers | `output\presentations\` or `output\reports\` |
| Articles, blog copies, landing pages | `output\pages\` |
| Research indices, SEO terms, analyses | `output\seo\` or `output\reports\` |
| Channel scheduling, social posts | `output\social\` |
