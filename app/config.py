import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="qwen/qwen3-32b",  # or qwen-qwq-32b
    api_key=os.getenv("GROQ_API_KEY")
)