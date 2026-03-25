# hr-policy-rag-chatbot
HR Policy RAG Chatbot is a FastAPI-based RAG application that ingests an HR Policy Manual PDF, chunks it, creates local embeddings with sentence-transformers, stores/searches them in Pinecone, and uses a Groq LLM to generate answers grounded in the retrieved policy text. It includes a simple web UI for chatting and supports local Docker deployment.
