from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from app.state import State
from app.nodes import tool_calling_llm
from app.tools import tools

def build_graph():
    builder = StateGraph(State)

    builder.add_node("llm", tool_calling_llm)
    builder.add_node("tools", ToolNode(tools))

    builder.add_edge(START, "llm")

    # LOOP until no tool needed
    builder.add_conditional_edges(
        "llm",
        tools_condition,
        {
            "tools": "tools",
            "__end__": END
        }
    )

    builder.add_edge("tools", "llm")

    return builder.compile()