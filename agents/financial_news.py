from langchain.agents import Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    temperature=0.3,
    model="gpt-3.5-turbo",
)

search_tool = DuckDuckGoSearchRun()

def summarize_news(topic: str) -> str:
    results = search_tool.run(topic)

    sysprompt = """
    You are a financial market assistant.

    Your task is to extract **only** the market-relevant insights from the provided search results, such as:
    - Earnings reports and numbers
    - Stock upgrades/downgrades
    - Analyst commentary
    - Company guidance
    - M&A, product launches **only if they are affecting stock**

    Ignore all marketing or hardware specs.

    Return 3–5 bullet points summarizing only market-impacting news.
    """

    prompt = [
        SystemMessage(content=sysprompt),
        HumanMessage(content=results)
    ]

    response = llm(prompt)
    return response.content

def news_agent_node(state: dict) -> dict:
    topic = state.get("input_prompt", "latest financial market news")
    summary = summarize_news(topic)
    return {
        **state,
        "news_summary": summary
    }