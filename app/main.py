from fastapi import FastAPI

app = FastAPI(title="InsureCompare API")


@app.get("/health")
def health_check():
    return {"status": "ok"}