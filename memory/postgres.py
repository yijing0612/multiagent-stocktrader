from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("POSTGRES_URL")

engine = create_engine(DB_URL)

def save_trade_to_postgres(ticker, news_summary, tech_signal, decision, confidence):
    with engine.connect() as conn:
        conn.execute(text("""
            INSERT INTO trade_memory (ticker, news_summary, technical_signal, decision, confidence)
            VALUES (:ticker, :news_summary, :tech_signal, :decision, :confidence)
        """), {
            "ticker": ticker,
            "news_summary":news_summary,
            "tech_signal": tech_signal,
            "decision": decision,
            "confidence": confidence
        })
        conn.commit()