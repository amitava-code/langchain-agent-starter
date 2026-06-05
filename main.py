from dotenv import load_dotenv
load_dotenv()

from tavily import TavilyClient
import os

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

result = tavily_client.search(query="What is the price of Bitcoin?")

print(result)