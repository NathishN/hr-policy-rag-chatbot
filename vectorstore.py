from pinecone import Pinecone
import os
from dotenv import load_dotenv
from typing import List, Dict, Any

#Load environment variables from .env file
load_dotenv()

#initialize Pinecone client
pinecone_client = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pinecone_client.Index(os.getenv("PINECONE_INDEX_NAME"))

def store_in_pinecone(chunks: List[str], embeddings: List[List[float]], namespace: str =""):
    vectors_to_upsert = []
    for i, (chunk,embedding) in enumerate(zip(chunks, embeddings)):
        vector_data = {
            "id": f"chunks_{i}",
            "values": embedding,
            "metadata": {
                "text": chunk,
                "chunk_index": i
            }
        }
        vectors_to_upsert.append(vector_data)

    #Upsert vectors in batches (Pinecone recommends batch size of 100)
    batch_size = 100
    for i in range(0, len(vectors_to_upsert), batch_size):
        batch = vectors_to_upsert[i:i + batch_size]
        index.upsert(vectors=batch, namespace=namespace)

def search_in_pinecone(query_vector: List[float], top_k: int = 5, namespace: str = "") -> List[str]:
    """Search pinecone and return matched chunk texts."""
    response: Dict[str, Any] = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True,
        namespace=namespace
    )
    matches = response.get("matches", [])
    return [match.get("metadata", {}).get("text", "") for match in matches if match.get("metadata")]
