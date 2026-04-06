import os
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from src.utils.embedding import embedd
from dotenv import load_dotenv

load_dotenv()

qd_api_key = os.getenv('QD_API_KEY')
qd_url = os.getenv('QD_URL')


def rag_search(query:str):
    client = QdrantClient(
        url=qd_url,
        api_key=qd_api_key
    )

    # retrieve the embedding vector of the user query from hugging face
    query_embedding = embedd(query=query)

    # retrieve the relevent texts from qdrant database
    try:
        hits = client.query_points(
            collection_name="indian_recipes",
            query=query_embedding,
            limit=3
        )
    except Exception as e:
        print(e)

    retrieved_recipes = ''
    for sp in hits.points:
        # print(sp.payload['recipe'])
        retrieved_recipes = retrieved_recipes + sp.payload['recipe']
    return retrieved_recipes