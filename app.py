import os
from dotenv import load_dotenv
from src.graph import recipeGraph
from langchain.messages import HumanMessage

load_dotenv()

response = recipeGraph.invoke({'messages': [HumanMessage(content='how to make butter chicken?')]})

chatbot = response['messages'][-1]

print(f"chatbot: {chatbot.content}")


