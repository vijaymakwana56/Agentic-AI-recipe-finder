import os
from langgraph.graph import START, END
from langgraph.graph.state import StateGraph
from src.nodes.agent_node import agent, tool_node, recipe_tools
from dotenv import load_dotenv
from src.state_graph import RecipeState
from langchain_core.messages import AIMessage


load_dotenv()

#conditional edge function to check if the graph is to end or not
def should_continue(state:RecipeState):
    last_message = state['messages'][-1]

    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return 'tools'
    
    return END


#intitialize the graph
recipeBuilder = StateGraph(RecipeState)

#adding the nodes to the graph
recipeBuilder.add_node('agent', agent)
recipeBuilder.add_node('tools', tool_node)

#adding edges to the nodes

recipeBuilder.add_edge(START, 'agent')
recipeBuilder.add_conditional_edges(
    'agent',
    should_continue,
    {'tools', END}
)
recipeBuilder.add_edge('tools', 'agent')


#compile the graph
recipeGraph = recipeBuilder.compile()