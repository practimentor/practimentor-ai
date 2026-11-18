from fastapi import FastAPI

app = FastAPI(title="practimentor-ai")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
