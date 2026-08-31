import os
import uuid

from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from app.services.extraction_service import extract_text_from_pdf
from app.services.cleanup_service import normalize_text
from app.services.parser_service import extract_total_premium
from app.services.parser_service import extract_policy_term_months
from app.services.compare_service import compare_premiums





router = APIRouter(prefix="/compare", tags=["compare"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def _validate_pdf(upload: UploadFile) -> None:
    if not upload.filename:
        raise HTTPException(status_code=400, detail="Missing filename")

    if not upload.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail=f"{upload.filename} is not a PDF")
@router.post("/upload")
async def upload_documents(
        dec_page: UploadFile = File(...),
        quote: UploadFile = File(...),
):
    _validate_pdf(dec_page)
    _validate_pdf(quote)
    comparison_id = f"{uuid.uuid4()}"
    dec_name = f"{comparison_id}_dec.pdf"
    quote_name = f"{comparison_id}_quote.pdf"

    dec_path = os.path.join(UPLOAD_DIR, dec_name)
    quote_path = os.path.join(UPLOAD_DIR, quote_name)

    dec_bytes = await dec_page.read()
    quote_bytes = await quote.read()

    with open(dec_path, "wb") as f:
        f.write(dec_bytes)
    with open(quote_path, "wb") as f:
        f.write(quote_bytes)

    return {
        "comparison_id": comparison_id,
        "files": {
            "dec_page": dec_name,
            "quote": quote_name,
        },
        "message": "File uploaded successfully",
    }
class ExtractRequest(BaseModel):
    comparison_id: str

@router.post("/extract")
def extract_documents(payload: ExtractRequest):
    dec_path = os.path.join(UPLOAD_DIR, f"{payload.comparison_id}_dec.pdf")
    quote_path = os.path.join(UPLOAD_DIR, f"{payload.comparison_id}_quote.pdf")

    if not os.path.exists(dec_path) or not os.path.exists(quote_path):
        raise HTTPException(status_code=400, detail="files not found for this comparison_id")

    dec_text = normalize_text(extract_text_from_pdf(dec_path))
    quote_text = normalize_text(extract_text_from_pdf(quote_path))
    dec_total_premium = extract_total_premium(dec_text)
    quote_total_premium = extract_total_premium(quote_text)
    dec_term_months = extract_policy_term_months(dec_text)
    quote_term_months = extract_policy_term_months(quote_text)
    premium_comparison = compare_premiums(dec_total_premium, quote_total_premium)
    return {
        "comparison_id": payload.comparison_id,
        "dec_page_chars": len(dec_text),
        "quote_chars": len(quote_text),
        "dec_preview": dec_text[:400],
        "quote_preview": quote_text[:400],
        "dec_total_premium": dec_total_premium,
        "quote_total_premium": quote_total_premium,
        "dec_term_months": dec_term_months,
        "quote_term_months": quote_term_months,
        "premium_comparison": premium_comparison,
    }