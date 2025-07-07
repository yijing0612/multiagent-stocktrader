# memory_writer.py

import yfinance as yf
from datetime import datetime
from sqlalchemy import text
from memory.postgres import engine

def fetch_current_price(ticker: str) -> float:
    try:
        ticker_data = yf.Ticker(ticker)
        return float(ticker_data.history(period="1d")["Close"].iloc[-1])
    except Exception as e:
        print(f"[Price Fetch Error] {e}")
        return None

def memory_writer_node(state: dict) -> dict:
    ticker = state.get("stock_ticker")
    news = state.get("news_summary")
    signal = state.get("quant_signal")
    decision = state.get("trade_decision")
    
    if not ticker or not news or not signal or not decision:
        return {**state, "memory_write_status": "Missing one or more fields"}

    now = datetime.now()
    price_at_trade = fetch_current_price(ticker)

    # Try to predict what price_after_trade *would* be after a day (optional logic)
    # For now, we fetch the same price again just to simulate testing logic
    price_after_trade = fetch_current_price(ticker)  # Replace with delayed fetch in real pipeline

    # Evaluate trade outcome
    trade_outcome = None
    if price_at_trade and price_after_trade:
        if "SELL" in decision.upper() and price_after_trade < price_at_trade:
            trade_outcome = "Successful"
        elif "BUY" in decision.upper() and price_after_trade > price_at_trade:
            trade_outcome = "Successful"
        else:
            trade_outcome = "Unsuccessful"

    with engine.begin() as conn:
        conn.execute(text("""
            INSERT INTO trade_memory (
                ticker, created_at, news_summary, technical_signal, decision,
                price_at_trade, price_after_trade, trade_outcome
            )
            VALUES (
                :ticker, :created_at, :news, :signal, :decision,
                :price_at_trade, :price_after_trade, :trade_outcome
            )
        """), {
            "ticker": ticker,
            "created_at": now,
            "news": news,
            "signal": signal,
            "decision": decision,
            "price_at_trade": price_at_trade,
            "price_after_trade": price_after_trade,
            "trade_outcome": trade_outcome
        })

    print(f"[Memory Writer] Saved trade for {ticker} @ {now.strftime('%Y-%m-%d %H:%M')}")
    if trade_outcome:
        print(f"[Memory Writer] Outcome evaluated: {trade_outcome}")

    return {**state, "memory_write_status": "Saved", "trade_outcome": trade_outcome}
