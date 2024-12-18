import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
EMBEDDING_MODEL = "BAAI/bge-small-en"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
VECTOR_INDEX = "compliance-vector-index"
