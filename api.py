from fastapi import FastAPI, Request
from pydantic import BaseModel
from main import app as langgraph_app

app_api = FastAPI()

class ChatRequest(BaseModel):
    user_message: str
    stock_ticker: str

@app_api.post("/chat")
def chat(req: ChatRequest):
    result = app.invoke({
        "input_prompt": req.user_message,
        "stocl_ticker": req.stock_ticker
    })

    return {
        "news_summary": result.get("news_summary"),
        "quant_signal": result.get("quant_signal"),
        "trade_decision": result.get("trade_decision"),
        "history_insights": result.get("history_insights"),
    }

from fastapi.middleware.cors import CORSMiddleware

app_api.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # change if deployed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)