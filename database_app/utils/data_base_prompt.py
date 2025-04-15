# prompt.py

def generate_analysis_prompt(stock_name: str) -> str:
    return f"""
You are a professional stock analyst. You are given daily time series data for {stock_name}, including:
- Open, High, Low, Close, Volume
- MA20 (20-day moving average)
- Daily_Return (day-over-day return)
- Volatility (High - Low)
- Momentum_5 (5-day momentum)
- Vol_MA5 (5-day average volume)

Based on these:
1. Identify trend vs MA20
2. Comment on recent volatility
3. Analyze momentum
4. Compare volume with Vol_MA5
5. Determine market phase (breakout, reversal, consolidation)

Return only the Markdown summary:

### {stock_name} Technical Summary  
- Trend: ...  
- Volatility: ...  
- Momentum: ...  
- Volume Support: ...  
- Market Phase: ...

**Conclusion:** ...
"""
