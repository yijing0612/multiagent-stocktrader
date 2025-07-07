from typing import TypedDict, Optional, Dict, List

class TradingState(TypedDict):
    input_prompt: str
    stock_ticker: str
    news_summary: Optional[str]
    quant_signal: Optional[Dict]
    trade_decision: Optional[str]
    memory: Optional[List[str]]
    history_insights: Optional[str]
    trade_outcome: Optional[str] = None