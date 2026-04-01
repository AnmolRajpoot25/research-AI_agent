import streamlit as st
from app.graph import build_graph
from langchain_core.messages import HumanMessage

# Initialize graph
graph = build_graph()

# Page config
st.set_page_config(page_title="AI Agent", page_icon="🤖", layout="wide")

st.title("🤖 AI Research Agent")
st.caption("Powered by Groq + Tavily + arXiv")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Ask anything...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from agent
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = graph.invoke({
                "messages": [HumanMessage(content=user_input)]
            })

            response = result["messages"][-1].content
            st.markdown(response)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})