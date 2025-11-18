import os
from dotenv import load_dotenv

load_dotenv()

# Gemini API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash-exp")
GEMINI_EMBEDDING_MODEL = os.getenv("GEMINI_EMBEDDING_MODEL", "models/text-embedding-004")

# Retrieval Configuration
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))
RETRIEVAL_TOP_K = int(os.getenv("RETRIEVAL_TOP_K", "4"))

# Hybrid Search Weights (vector_weight, bm25_weight)
VECTOR_WEIGHT = float(os.getenv("VECTOR_WEIGHT", "0.5"))
BM25_WEIGHT = float(os.getenv("BM25_WEIGHT", "0.5"))

# Agentic Workflow Configuration
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "2"))
TEMPERATURE = float(os.getenv("TEMPERATURE", "0"))

# Paths
DATA_DIR = os.getenv("DATA_DIR", "./data")
INDICES_DIR = os.getenv("INDICES_DIR", "./indices")
FAISS_INDEX_PATH = os.path.join(INDICES_DIR, "faiss_index")
BM25_INDEX_PATH = os.path.join(INDICES_DIR, "bm25_index.pkl")
