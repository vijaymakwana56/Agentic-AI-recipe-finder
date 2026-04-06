import os
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from dotenv import load_dotenv

load_dotenv()

QD_API_KEY = os.getenv('QD_API_KEY')

def rag_search(query:str):
    pass