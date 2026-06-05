from dotenv import load_dotenv
load_dotenv()

from tavily import TavilyClient
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage
import os

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def surfInternet(query:str):
    """Use this tool for getting the latest information from the internet."""

    result = tavily_client.search(query=query)

    return str(result)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

agent = create_agent(model=model, tools=[surfInternet])

response = agent.invoke({"messages": [HumanMessage("Who is the current president of the United States as of today?")]})
print(response["messages"][-1].text)