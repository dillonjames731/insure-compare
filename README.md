### InsureCompare: AI-Powered Insurance Policy & Quote Comparison Tool
InsureCompare is a Python/FastAPI backend project that lets users upload an insurance declarations page and a new quote, extract key information, and compare differences in plain language.

### Why I Built This
I built this project to practice real-world backend engineering for internship preparation, combining API design, document parsing, and AI-oriented product thinking.

### Current Features (v1)
- `GET /health` health-check endpoint
- `POST /compare/upload` to upload two PDF documents
- `POST /compare/extract` to extract and normalize text from uploaded documents
- Parsing of key fields when present:
  - total premium
  - policy term (months)
- Premium comparison summary output

### Tech Stack
- Python
- FastAPI
- Pydantic
- pdfplumber
- Uvicorn

### Project Structure
- `app/api/` → API route handlers
- `app/services/` → extraction, cleanup, parsing, and comparison logic
- `app/models/` → request/response model definitions
- `tests/` → test files

### How to Run Locally
```bash
python3 -m pip install fastapi uvicorn python-multipart pdfplumber pydantic
python3 -m uvicorn app.main:app --reload