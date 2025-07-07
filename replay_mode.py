from langgraph.graph import StateGraph
from state.schema import TradingState
from agents.history_analyzer import history_agent_node
import json
from langgraph.memory import MemorySaver
from dotenv import load_dotenv
load_dotenv()

graph = StateGraph(TradingState)
graph.add_node("history_agent", history_agent_node)
graph.set_entry_point("history_agent")
graph.set_finish_point("history_agent")

graph.add_memory(
    memory=MemorySaver.from_defaults(
        redis_url=os.getenv("REDIS_URL"),
        session_id="nvda-session-001"
    )
)

app = graph.compile()

if __name__ == "__main__":
    result = app.invoke({
        "input_prompt": "replay",  
        "stock_ticker": "NVDA",    
    })

    print("\n--- [Debug] Full Result Dict ---")
    print(json.dumps(result, indent=2))

    print("\n--- Strategy Insight from History ---")
    print(result.get("history_insights"))