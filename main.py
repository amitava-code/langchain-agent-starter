from dotenv import load_dotenv
load_dotenv()

from tavily import TavilyClient
from langchain.tools import tool
import os

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def surfInternet(query:str):
    """"USe this tool for getting the latest information from the internet"""

    result = tavily_client.search(query=query)

    print(result)


surfInternet.invoke({"query":"Kolkata News"})