from dotenv import load_dotenv
from typing import List
from sentence_transformers import SentenceTransformer

load_dotenv()

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
model = SentenceTransformer(EMBEDDING_MODEL)

def embed_documents(documents: List[str]) -> List[List[float]]:
    """Embed a list of document chunks with a local model."""
    if not documents:
        return []
    vectors = model.encode(documents, normalize_embeddings=True).tolist()
    return vectors

def embed_user_query(query: str) -> List[float]:
    """Embed a single user query with the same model used for documents."""
    return model.encode(query, normalize_embeddings=True).tolist()

# Backward-compatible alias for older imports
def embed_User_query(query: str) -> List[float]:
    return embed_user_query(query)
