from sqlalchemy import text
import textwrap
from memory.postgres import engine
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo")

def fetch_recent_trades(ticker: str, limit: int = 5) -> str:
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT created_at, news_summary, technical_signal, decision
            FROM trade_memory
            WHERE ticker = :ticker
            ORDER BY created_at DESC
            LIMIT :limit
        """), {"ticker": ticker, "limit": limit})
        rows = result.fetchall()

    print(f"\n--- [Debug] Fetched {len(rows)} trades for {ticker} ---")

    if not rows:
        return None

    history = "\n".join([
        f"{r.created_at.strftime('%Y-%m-%d')}: {r.decision} | Signal: {r.technical_signal}\nNews: {r.news_summary[:120]}..."
        for r in rows
    ])

    print("\n--- [Debug] Trade History String ---")
    print(history)

    return history

def analyze_trade_history(ticker: str) -> str:
    history = fetch_recent_trades(ticker)

    if not history:
        return f"No trade history found in database for {ticker}."

    prompt = [
        SystemMessage(content="""
        You are a trading strategy analyst.

        Analyze the user's recent trades for mistakes, overfitting, or missed opportunities.

        Suggest strategy refinements based on observed patterns.
        """),
        HumanMessage(content=history)
    ]

    return llm.invoke(prompt).content


def history_agent_node(state: dict) -> dict:
    ticker = state.get("stock_ticker")
    print("\n--- [Debug] History Agent Ticker ---")
    print("Ticker:", ticker)

    if not ticker:
        return {**state, "history_insights": "Missing 'stock_ticker'. Cannot analyze history."}

    insights = analyze_trade_history(ticker)

    print("\n--- [Debug] History Insights Generated ---")
    print(insights)

    return {
        **state,
        "history_insights": insights
    }
