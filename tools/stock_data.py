import yfinance as yf

def get_stock_indicators(ticker: str) -> dict:
    data = yf.Ticker(ticker)
    hist = data.history(period="6mo")

    if hist.empty:
        return {}
    
    close = hist["Close"]
    rsi = compute_rsi(close)

    indicators = {
        "current_price": close.iloc[-1],
        "50_MA": close.rolling(window=50).mean().iloc[-1],
        "150_MA": close.rolling(window=150).mean().iloc[-1],
        "200_MA": close.rolling(window=200).mean().iloc[-1],
        "RSI": rsi.iloc[-1]
    }

    indicators["technical_signal"] = evaluate_technical_signal(indicators)

    return indicators

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1+rs))

def evaluate_technical_signal(data: dict) -> str:
    price = data["current_price"]
    above_50 = price > data["50_MA"]
    above_150 = price > data["150_MA"]
    above_200 = price > data["200_MA"]
    rsi = data["RSI"]

    momentum = sum([above_50, above_150, above_200])
    
    if momentum >= 2 and rsi < 70:
        return "strong_uptrend"
    elif momentum <= 1 and rsi > 70:
        return "overbought_downtrend"
    elif rsi < 30:
        return "oversold_potential"
    else:
        return "unclear"