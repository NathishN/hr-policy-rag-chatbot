"""
app.py — FastAPI backend for the HR Policy RAG Chat Interface
Run with: uvicorn app:app --reload --port 8000
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from QueryProcessor import process_user_query

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="HR Policy RAG API")

# Allow the HTML frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Restrict in production
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str


@app.get("/")
def root():
    """Serve the chat UI so http://127.0.0.1:8000/ is not 404."""
    html_path = BASE_DIR / "hr_policy_chat.html"
    if not html_path.is_file():
        raise HTTPException(
            status_code=404,
            detail=f"Missing {html_path.name} next to app.py.",
        )
    return FileResponse(html_path, media_type="text/html")


@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    try:
        answer = process_user_query(request.query)
        return QueryResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok", "model": "llama-3.1-8b-instant", "embedding": "all-MiniLM-L6-v2"}
