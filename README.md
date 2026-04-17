🧠 HR Policy RAG Chat Assistant
A production-ready Retrieval-Augmented Generation (RAG) system that enables employees to query HR policies conversationally and receive accurate, context-grounded answers.

This system ingests HR policy documents, converts them into embeddings, retrieves the most relevant policy sections, and generates precise responses using an LLM — eliminating guesswork and reducing HR dependency.

🚀 Overview
HR Policy RAG Chat Assistant is designed to solve a simple but expensive problem:

Employees don’t read policy documents — but they still need correct answers.

Instead of forcing users to search through PDFs, this system:

Understands their question

Retrieves the exact relevant policy sections

Generates a grounded, accurate response

No hallucinations. No vague answers. Just policy-backed responses.

🏗️ Architecture
Pipeline Flow:

PDF → Chunking → Embeddings → Pinecone → Retrieval → LLM → Response
Core Components
Document Ingestion

Extracts text from HR policy PDFs

Splits content into overlapping chunks

Generates embeddings using sentence-transformers

Stores vectors in Pinecone

Retrieval Layer

Performs semantic search

Fetches top-k relevant policy chunks

Generation Layer

Uses Groq-hosted LLM

Constrains responses strictly to retrieved context

API Layer

FastAPI backend for interaction

Frontend

Lightweight chat interface (hr_policy_chat.html)

⚙️ Tech Stack
Layer	Technology
Backend API	FastAPI
LLM	Groq
Embeddings	Sentence-Transformers
Vector Database	Pinecone
Document Parsing	pypdf
Deployment	Docker
🔑 Key Features
✅ PDF ingestion with automated chunking

✅ Semantic search using vector embeddings

✅ Context-aware responses (no blind generation)

✅ FastAPI-based scalable backend

✅ Clean and simple chat UI

✅ Docker support for easy deployment
