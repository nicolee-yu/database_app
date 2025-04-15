# get_data.py

import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    # 支持单个或多个股票输入（如 "AAPL", "AAPL MSFT TSLA"）
    tickers = [t.strip() for t in ticker.replace(",", " ").split()]
    df = yf.download(tickers, start=start, end=end, group_by="ticker" if len(tickers) > 1 else None)

    # 统一列名：展开 MultiIndex 为单层
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = ['_'.join(col).strip() for col in df.columns]

    return df

def compute_indicators(df: pd.DataFrame, ticker: str) -> pd.DataFrame:
    ticker = ticker.upper()

    # 以 AAPL_Close 风格拼接列名
    close_col = f"{ticker}_Close"
    high_col = f"{ticker}_High"
    low_col = f"{ticker}_Low"
    volume_col = f"{ticker}_Volume"

    # 添加技术指标
    df["MA20"] = df[close_col].rolling(window=20).mean()
    df["Daily_Return"] = df[close_col].pct_change()
    df["Volatility"] = df[high_col] - df[low_col]
    df["Momentum_5"] = df[close_col] - df[close_col].shift(5)
    df["Vol_MA5"] = df[volume_col].rolling(window=5).mean()

    # 为绘图简化一列
    df.rename(columns={close_col: "Close"}, inplace=True)

    return df.dropna()


