from langgraph.graph.message import add_messages, BaseMessage
from typing import TypedDict, Annotated, Literal

class RecipeState(TypedDict):
    #storing the chat history with the agent in list
    messages: Annotated[list[BaseMessage], add_messages]

    #user query
    query: str

    #to store the last used tool for the current chat
    last_tool: Literal["rag", "web"]

    #storing the rag or the web results as a string
    rag_result: str
    web_result: str
    
    #storing the final results
    recipe: str