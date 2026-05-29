import os
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DATA_DIR = os.getenv("DATA_DIR", "/tmp/data")
CHROMA_PATH = "vectordb"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2" # Modelo de embeddings local
LLM_MODEL = "llama-3.3-70b-versatile" # Modelo de Groq
