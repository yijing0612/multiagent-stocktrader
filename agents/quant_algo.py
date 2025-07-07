from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv
from tools.stock_data import get_stock_indicators
import os

load_dotenv()

llm = ChatOpenAI(
    temperature=0.2,
    model="gpt-3.5-turbo",
)

def generate_quant_signal(news_summary: str) -> dict:
    sysprompt = """
    You are a quantitative financial analyst assistant.
    
    You are given:
    - A summarized financial news section
    - A set of technical indicators for a stock
    - A derived "technical signal" label (e.g., strong_uptrend, oversold_potential, overbought_downtrend)

    Determine:
    - Whether the stock is a BUY, SELL, or HOLD
    - Your confidence (0-1)
    - Explain in 1-2 lines using both news + indicators

    Rules:
    - If news is positive AND signal is "strong_uptrend" → "buy"
    - If RSI > 70 and signal is weak → "sell"
    - If RSI < 30 and news is positive → "buy"
    - If indicators contradict news → "hold"
    - If signal is "unclear" or sentiment is neutral → "hold"

    Return JSON:
    {
    "signal": "...",
    "confidence": 0.X,
    "reason": "..."
    }
    """

    prompt = [
        SystemMessage(content=sysprompt),
        HumanMessage(content=news_summary)
    ]

    response = llm(prompt)

    try:
        return eval(response.content.strip())
    except Exception as e:
        print("Error parsing signal:", e)
        return {"signal": "hold", "confidence": 0.5, "reason": "Parsing error"}
    
def quant_agent_node(state: dict) -> dict:
    news = state.get("news_summary", "")
    ticker = state.get("stock_ticker", "")

    indicators = get_stock_indicators(ticker)
    if not indicators:
        return {
            **state,
            "quant_signal": {
                "signal": "hold",
                "confidence": 0.5,
                "reason": "No indicator data available"
            }
        }

    # Create LLM prompt combining both news and indicators
    prompt_text = f"""
        News Summary:
        {news}

        Technical Indicators for {ticker}:
        - Current Price: {indicators['current_price']}
        - 50 MA: {indicators['50_MA']}
        - 150 MA: {indicators['150_MA']}
        - 200 MA: {indicators['200_MA']}
        - RSI: {indicators['RSI']}
        - Technical Signal: {indicators['technical_signal']}
    """

    signal = generate_quant_signal(prompt_text)

    return {
        **state,
        "quant_signal": signal
    }