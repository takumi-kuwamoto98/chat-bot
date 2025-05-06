from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from utils.state import State
from nodes.chat_bot import chatbot
from nodes.tool_node import tool_node
from edges.root_tool import route_tools

graph_builder = StateGraph(State)
graph_builder.add_node("tools", tool_node)
graph_builder.add_node("chatbot", chatbot);
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("tools", "chatbot");
# graph_builder.add_edge("chatbot", END);
graph_builder.add_conditional_edges("chatbot", route_tools, {"tools": "tools", END: END})
graph = graph_builder.compile();


def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass

while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
    except:
        # fallback if input() is not available
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break

