from fastapi import FastAPI

app = FastAPI(title="utp-agent-api-rag")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
