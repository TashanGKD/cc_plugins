---
name: scispark
description: Execute the 7-stage Scispark workflow to generate a high-quality, verifiable research idea from a keyword
version: 0.1.0
tags:
  - research
  - workflow
  - academic
  - literature
dependencies:
  article-mcp: ">=0.1.0"
  sequentialthinking: ">=0.1.0"
---

# Scispark Research Idea Generation

Execute the 7-stage Scispark workflow to generate a high-quality, verifiable research idea from a keyword.

## Usage

```
/scispark <keyword> [options]
```

## Arguments

- **keyword** (required): Research topic keyword to generate ideas for
- **options** (optional):
  - `--skip-slides` - Skip stage 7 (slide generation)
  - `--min-papers <n>` - Set minimum paper threshold (default: 30)
  - `--quick-mode` - Quick mode with simplified analysis
  - `--target <stage>` - Stop at specific stage (1-6)

## Examples

```
/scispark "hybrid speciation"
/scispark "CRISPR gene editing" --skip-slides
/scispark "climate adaptation" "hybrid zones" --min-papers 20
/scispark "plant immunity" --quick-mode
/scispark "genomic imprinting" --target 4
```

## What it does

The workflow executes 7 stages to transform a keyword into a research idea:

1. **Fact Extraction** - Extract structured facts from 30+ full-text papers
2. **Hypothesis Generation** - Generate 3-5 verifiable research hypotheses
3. **Initial Idea** - Combine hypotheses into initial research concept
4. **Technical Optimization** - Optimize methods with Review cycle
5. **MoA Optimization** - Deepen mechanism of action analysis
6. **Human-AI Collaboration** - Final integration with academic standards check
7. **Slide Generation** (optional) - Generate Quarto academic slides

## Output

Generated files in `03-AI笔记/scispark/{keyword}/`:

| File | Description |
|------|-------------|
| `experts/01_domain_overview.md` | Domain expert overview |
| `01_fact_extraction.md` | Structured facts from literature |
| `02_hypothesis.md` | Research hypotheses (H1-H5) |
| `03_initial_idea.md` | Initial research concept |
| `04_technical_optimization.md` | Technical method optimization |
| `05_moa_optimization.md` | Mechanism of action analysis |
| `06_human_ai_collaboration.md` | Final integration details |
| `{keyword}_final_idea.md` | **Final research idea** |
| `literature.csv` | Complete literature tracking |
| `slides/` | Quarto presentation (optional) |

## Literature Requirements

| Threshold | Full-text Papers | Mode | Use Case |
|-----------|------------------|------|----------|
| Ideal | ≥50 | Deep analysis | Mature fields |
| Standard | ≥30 | Standard analysis | Most fields |
| Minimum | ≥15 | Basic + limitations | Niche fields |
| Abort | <15 | Error - suggest new keywords |

## Review Mechanism

Stages 4-6 include Review cycles:
1. **Evaluate current version** - Identify pros/cons
2. **Extract optimization directions** - Generate improvement suggestions
3. **Search supplementary literature** - Support optimization decisions
4. **Iterative optimization** - Improve based on review findings

## Expert System Integration

| Timing | Expert Type | Output |
|--------|-------------|--------|
| Before Stage 1 | Domain Expert | Field overview, theoretical foundations |
| Before Stage 4 | Methodology Expert | Technical method assessment |
| Before Stage 5 | Mechanism Expert | MoA depth evaluation |
| Before Stage 6 | Integrated Expert | Overall feasibility assessment |

## Requirements

This command requires the following MCP servers:
- **article-mcp** - Literature search
- **sequentialthinking** - Structured analysis

Optional tools:
- Local `.tashan/index.json` - Literature library
- `pdfget` - Paper download
- `literature-watcher` - Auto monitoring
- `literature-summarizer` - Generate summaries

## Academic Standards

- **Citation format**: `[number]` in-text, Nature journal style for references
- **Language**: Objective, cautious, academic tone
- **No**: absolute terms ("first", "breakthrough"), emojis, non-academic symbols
- **Yes**: "This study", cautious language, proper terminology

## Execution Time

- **Quick mode**: 10-15 minutes
- **Standard mode**: 30-45 minutes
- **Full with slides**: 45-60 minutes

## Notes

- All literature citations include PMID/DOI when available
- Literature CSV tracks complete usage history across all stages
- Academic standards check performed in Stage 6
- Generated slides use Quarto + reveal.js format

## Troubleshooting

**Q: Literature insufficient (<15 papers)?**
A: System will suggest alternative keywords or broader search terms.

**Q: Quick mode quality?**
A: Quick mode uses lower thresholds (15-20 papers) with limitations noted.

**Q: How to continue from saved state?**
A: Use `--target <stage>` to resume from specific stage.
