import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from src.tools.rag_search import rag_search_recipe
from src.tools.web_search import web_search_tool
from src.state_graph import RecipeState
from langchain.messages import SystemMessage

#loading the variables
load_dotenv()
groq_model = os.getenv('G_MODEL')
groq_api_key = os.getenv('GROQ_API_KEY')

recipe_tools = [rag_search_recipe, web_search_tool]

#initialize the groq llm
llm = ChatGroq(model=groq_model, temperature=0.5, verbose=True).bind_tools(tools=recipe_tools)

def agent(state:RecipeState):
    # 1. Define the Persona/System Instructions
    # This ensures the LLM knows about your specific tools (RAG vs Web)
    system_instruction = SystemMessage(content=(
        "You are an expert Chef AI. Your goal is to provide accurate recipes."
        "First, always try to use 'rag_search_recipe' to find high-quality, curated recipes."
        "If 'rag_search_recipe' does not return a satisfactory result, use 'web_search_tool'."
        "Maintain a helpful and professional culinary tone."
    ))
    inputs = [system_instruction] + state["messages"]

    try:
        # The .invoke() here will return an AIMessage containing either
        # a direct response or tool_calls.
        response = llm.invoke(input=inputs)

        return {
            'message': [response],
            'query': state.get('query') #to ensure that the state query persists
        }

    except Exception as e:
        # In production, log this to a service like Sentry or CloudWatch
        print(f"Error in agent_node: {str(e)}")
        
        # Return a graceful failure message to the user
        return {
            "messages": [SystemMessage(content="I'm sorry, I'm having trouble connecting to my brain right now. Please try again.")]
        }