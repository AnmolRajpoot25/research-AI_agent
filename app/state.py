from typing import TypedDict, List
from langchain_core.messages import BaseMessage

class State(TypedDict):
    messages: List[BaseMessage]