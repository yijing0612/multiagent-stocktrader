def trader_agent_node(state: dict) -> dict:
    signal = state.get("quant_signal", {})
    action = signal.get("signal", "hold")
    reason = signal.get("reason", "No reason provided.")
    confidence = signal.get("confidence", 0.5)

    decision = f"Executing {action.upper()} order. Confidence: {confidence:.2f}. Reason: {reason}"

    return {
        **state,
        "trade_decision": decision
    }