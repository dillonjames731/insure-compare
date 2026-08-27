from fastapi import FastAPI
from app.api.upload import router as upload_router

app = FastAPI(title="InsureCompare API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(upload_router)