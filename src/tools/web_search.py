import os
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()


def web_search_tool(query:str):
    # web search using tavily to get top 2 best results from the results.
    try:
        #initialize the searchtool
        tavily = TavilySearch(
        include_raw_content=True,
        search_depth="advanced",
        max_results = 2,
        )

        response = tavily.invoke({"query":query})

        cleaned_results = [recipe['raw_content'][:20000] for recipe in response['results']]

        return cleaned_results
    
    except Exception as e:
        return f"The search tool failed with the error{str(e)}"
