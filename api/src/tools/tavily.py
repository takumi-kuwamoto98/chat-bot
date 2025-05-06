from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os

load_dotenv()
apiKey = os.getenv("TAVILY_API_KEY")
if not apiKey:
    raise ValueError("TAVILY_API_KEY is not set")

tool = TavilySearch(max_results=2, api_key=apiKey)
