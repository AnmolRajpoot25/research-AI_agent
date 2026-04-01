import os
from langchain_tavily import TavilySearch
from langchain.tools import tool
import arxiv
from app.utils import retry

# 🔍 Tavily Tool
tavily = TavilySearch(
    tavily_api_key=os.getenv("TAVILY_API_KEY")
)


# 📄 Custom arXiv Tool (SAFE)
@tool
def arxiv_search(query: str) -> str:
    """Search research papers from arXiv"""

    def run():
        search = arxiv.Search(
            query=query,
            max_results=3
        )

        results = []
        for r in search.results():
            results.append(
                f"Title: {r.title}\nSummary: {r.summary[:500]}"
            )

        return "\n\n".join(results)

    return retry(run)


# 🔗 Tool list
tools = [tavily, arxiv_search]