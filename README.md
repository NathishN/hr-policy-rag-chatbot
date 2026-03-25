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

📦 Project Structure
hr-policy-rag-chatbot/
│
├── app/
│   ├── main.py                # FastAPI entry point
│   ├── routes/               # API endpoints
│   ├── services/             # RAG pipeline logic
│
├── ingestion/
│   ├── pdf_loader.py         # PDF parsing
│   ├── chunking.py           # Text splitting
│   ├── embedding.py          # Embedding generation
│
├── vectorstore/
│   ├── pinecone_client.py    # Pinecone integration
│
├── frontend/
│   ├── hr_policy_chat.html   # Chat UI
│
├── Dockerfile
├── requirements.txt
└── README.md
🔌 API Endpoints
Health Check
GET /health
Ask a Question
POST /ask
Request:

{
  "question": "What is the leave policy?"
}
Response:

{
  "answer": "Employees are entitled to 20 days of annual leave..."
}
🧪 Local Development
1. Clone the Repository
git clone https://github.com/your-repo/hr-policy-rag-chatbot.git
cd hr-policy-rag-chatbot
2. Install Dependencies
pip install -r requirements.txt
3. Set Environment Variables
export PINECONE_API_KEY=your_key
export GROQ_API_KEY=your_key
4. Run the Server
uvicorn app.main:app --reload
5. Open UI
Open frontend/hr_policy_chat.html in your browser.

🐳 Docker Deployment
Build Image
docker build -t hr-rag-bot .
Run Container
docker run -p 8000:8000 hr-rag-bot
🎯 Use Cases
HR policy Q&A automation

Employee onboarding support

Internal knowledge base assistant

Compliance clarification

⚠️ Limitations (Don’t Ignore This)
If you deploy this blindly, it will fail in these scenarios:

Poorly written or outdated HR documents → garbage answers

Bad chunking strategy → context loss

No metadata filtering → irrelevant retrieval

Over-reliance on top-k retrieval → missed edge cases

Fix these before scaling:

Add metadata (department, policy type)

Tune chunk size & overlap

Implement re-ranking

Add evaluation metrics (precision, recall)

🔮 Future Improvements
Multi-document support

Role-based access control

Feedback loop for answer correction

Hybrid search (keyword + vector)

UI upgrade (React-based dashboard)

🧠 Bottom Line
This is not “just another chatbot.”

It’s a decision-support system:

Grounded in real policy

Scalable across organizations

Replaceable for manual HR queries

If it’s giving wrong answers, the issue isn’t the model —
it’s your retrieval pipeline. Fix that first.
