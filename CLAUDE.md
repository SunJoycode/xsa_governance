# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI XSA Governance Publisher — reads SAP HANA XSA SQLScript procedures, uses Claude AI to explain business logic, then publishes semantic metadata to **Collibra** and **Ellie.ai** governance platforms.

## Running the Application

```bash
# Setup: copy and populate environment variables
cp .env.example .env

# Run via Docker (recommended)
docker-compose up

# Run directly
python app/main.py
```

No test or lint commands are configured.

## Environment Variables (`app/config.py`)

| Variable | Purpose |
|---|---|
| `ANTHROPIC_API_KEY` | Claude API authentication |
| `COLLIBRA_URL` / `COLLIBRA_TOKEN` | Collibra governance platform |
| `ELLIE_URL` / `ELLIE_TOKEN` | Ellie.ai governance platform |

## Architecture

The app runs a linear pipeline orchestrated by `app/main.py`:

```
xsa_docs/ (.hdbprocedure files)
  → agents/xsa_loader.py       # Scans folder, reads SQLScript files
  → agents/claude_explainer.py  # Claude AI extracts: purpose, tables, metrics, formula
  → agents/semantic_builder.py  # Converts to JSON, writes to outputs/semantic/
  → publishers/collibra_publisher.py  # POST to Collibra as "Data Product" asset
  → publishers/ellie_publisher.py     # POST model to Ellie.ai
```

### Key Details

- **AI model**: `claude-3-sonnet-20240229`, temperature 0.2, max 1500 tokens
- **Input files**: `.hdbprocedure` files (SAP HANA SQLScript) — place in `xsa_docs/` (the `load_xsa()` call in `main.py` references `"sample_xsa"` but this folder doesn't exist; update the path or rename the folder)
- **Output**: JSON semantic files written to `outputs/semantic/{filename}.json`
- **Publishers**: Both Collibra and Ellie publishers use bearer token auth via REST API; no error handling on HTTP calls

### FastAPI / Uvicorn

These are in `requirements.txt` but not currently used — they appear to be scaffolding for a future REST API layer.
