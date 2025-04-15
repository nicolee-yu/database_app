# streamlit_app.py


import openai
from utils.data_base_recommend import fetch_stock_data, compute_indicators
from utils.data_base_prompt import generate_analysis_prompt
import pandas as pd

import streamlit as st
import datetime


# streamlit_app.py



# 模拟 AI 分析函数（可替换为 OpenAI API）
def simulate_ai_analysis(ticker: str) -> str:
    return f"""
### {ticker.upper()} Technical Summary  
- **Trend**: Uptrend (price above rising MA20)  
- **Volatility**: Increasing, signaling stronger price swings  
- **Momentum**: Positive but weakening slightly  
- **Volume Support**: Strong (volume above 5-day average)  
- **Market Phase**: Breakout continuation  

**Conclusion:** {ticker.upper()} shows signs of sustained upward momentum supported by strong volume and increasing volatility, though slight momentum flattening may warrant short-term caution.
"""

# Streamlit 页面入口
st.title("📈 AI Stock Technical Analyzer (Multi-symbol Demo)")

ticker_input = st.text_input("Enter stock ticker(s) (e.g., AAPL or AAPL MSFT TSLA):", value="AAPL")
start_date = st.date_input("Start Date", datetime.date(2023, 1, 1))
end_date = st.date_input("End Date", datetime.date.today())

if st.button("Analyze"):
    with st.spinner("Loading and analyzing..."):
        df_raw = fetch_stock_data(ticker_input, str(start_date), str(end_date))
        if df_raw.empty:
            st.warning("⚠️ No data found for these symbols.")
        else:
            tickers = [t.strip() for t in ticker_input.replace(",", " ").split()]
            for ticker in tickers:
                st.subheader(f"📍 {ticker.upper()}")
                df = compute_indicators(df_raw.copy(), ticker)
                if "Close" in df.columns and "MA20" in df.columns:
                    st.line_chart(df[["Close", "MA20"]])
                else:
                    st.warning(f"{ticker}: Missing necessary data columns.")
                    st.write(df.columns.tolist())

                st.markdown("### 📊 AI Analysis (Simulated)")
                st.markdown(simulate_ai_analysis(ticker))
