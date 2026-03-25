# HR Policy RAG API — FastAPI + local embeddings (CPU)
# Build:  docker build -t hr-rag .
# Run:    docker run --env-file .env -p 8000:8000 hr-rag
# Ingest (optional, if you mount PDF + run once):
#   docker run --env-file .env -v "%cd%:/data" hr-rag python dataprocessor.py

FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    HF_HOME=/cache/huggingface \
    TRANSFORMERS_CACHE=/cache/huggingface

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Warm the embedding model into the image (faster container startup; larger image).
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

RUN useradd --create-home --uid 1000 appuser
RUN chown -R appuser:appuser /app /cache
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
