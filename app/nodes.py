from app.config import llm
from app.tools import tools

llm_with_tools = llm.bind_tools(tools)

def tool_calling_llm(state):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}