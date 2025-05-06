import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from tools.tavily import tool

load_dotenv()
apiKey = os.getenv("OPENAI_API_KEY")
if not apiKey:
    raise ValueError("OPENAI_API_KEY is not set")

llm = ChatOpenAI(model="gpt-4o-mini", api_key=apiKey)
llm_with_tools = llm.bind_tools([tool])




# The first argument is the unique node name
# The second argument is the function or object that will be called whenever
# the node is used.
