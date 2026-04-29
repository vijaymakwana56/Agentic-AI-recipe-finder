import os
from dotenv import load_dotenv
from src.graph import recipeGraph
from langchain.messages import HumanMessage

load_dotenv()

response = recipeGraph.invoke({'messages': [HumanMessage(content='how to make khaman?')]})

chatbot = response['messages'][-1]

print(f"chatbot: {chatbot.content}")

# for message_chunk, metadata  in recipeGraph.stream(
#     {'messages': [HumanMessage(content='how to make khaman?')]},
#     stream_mode= 'messages'
# ):
#     if message_chunk.content:
#         print(message_chunk.content, end=" ", flush=True)

