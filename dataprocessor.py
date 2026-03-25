from pypdf import PdfReader
from pdfreader import read_pdf
from chunker import chunk_pages
from dotenv import load_dotenv
from embedder import embed_documents
from vectorstore import store_in_pinecone
from typing import List
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
pdf_path = BASE_DIR / "resources" / "NexaBridge_HR_Policy_Manual.pdf"

def run():
    # Read HR Policy Manual PDF
    pages = read_pdf(str(pdf_path))

    # Chunk the data into smaller pieces
    chunks = chunk_pages(pages)

    # Embed chunks locally to create vector representations
    embeddings = embed_documents(chunks)

    # Store the chunks and their embeddings in Pinecone vector database
    store_in_pinecone(chunks, embeddings)

if __name__ == "__main__":
    run()