from utils.llm import llm_with_tools
from utils.state import State

def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}