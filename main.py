from app.graph import build_graph
from langchain_core.messages import HumanMessage

graph = build_graph()

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    result = graph.invoke({
        "messages": [HumanMessage(content=query)]
    })

    print("AI:", result["messages"][-1].content)