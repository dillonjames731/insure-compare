import os
import uuid

from fastapi import APIRouter, UploadFile, File, HTTPException


router = APIRouter(prefix="/compare", tags=["compare"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def _validate_pdf(upload: UploadFile) -> None:
    if not upload.filename:
        raise HTTPException(status_code=400, detail="Missing filename")

    if not upload.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail=f"{upload.filename} is not a PDF")
@router.post("/upload", tags=["upload"])
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