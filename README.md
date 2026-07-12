# AI Clinical Evidence and Literature Review Automation

Production-oriented reference implementation for IVD clinical evidence surveillance, systematic literature review, evidence extraction, appraisal, and controlled report drafting.

## Architecture
- React + TypeScript review workspace
- Node.js + Express workflow API
- Python + FastAPI evidence service
- PubMed/NCBI E-utilities connector
- Azure AI Search evidence index
- Azure Blob Storage source archive
- Azure OpenAI grounded extraction and synthesis
- Microsoft Entra ID, RBAC, immutable audit records

## Guardrails
AI output is advisory. Screening exclusions, evidence appraisal, clinical conclusions, and report approval require qualified human review.

## Run locally
```bash
cp .env.example .env
docker compose up --build
```
Open `http://localhost:5173`.