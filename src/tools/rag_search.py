import os
from qdrant_client import QdrantClient
from src.utils.embedding import embedd
from dotenv import load_dotenv

load_dotenv()


class RagTool:

    def __init__(self):
        self.qd_api_key = os.getenv('QD_API_KEY')
        self.qd_url = os.getenv('QD_URL')
        self.client = QdrantClient(
            url=self.qd_url,
            api_key=self.qd_api_key
        )

    def rag_search(self,query:str)->str:
        
        try:
            # retrieve the embedding vector of the user query from hugging face
            query_embedding = embedd(query=query)

            # retrieve the relevent texts from qdrant database
            hits = self.client.query_points(
                collection_name="indian_recipes",
                query=query_embedding,
                limit=3
            )
            
            #Each of the recieved recipe processed and concatenated
            retrieved_recipes = "\n\n".join(
                [r.payload['recipe'] for r in hits.points if 'recipe' in r.payload
            ])

            return retrieved_recipes

        except Exception as e:
            print(e)