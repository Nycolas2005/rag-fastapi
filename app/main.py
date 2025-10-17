from fastapi import FastAPI
from app.api.v1.rag import router as rag_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="RAG API", version="1.0.0")
app.include_router(rag_router, prefix="/api/v1")
