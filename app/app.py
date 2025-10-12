import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date

# --- 1. ANALYSIS HELPER FUNCTION (Copy/Paste from Section 1) ---
def get_analyzed_data(ticker, start_date, end_date):
    # ... (Paste the function code here in the actual app.py file)
    df = yf.download(ticker, start=start_date, end=end_date)
    if df.empty:
        return None
    df.columns = df.columns.get_level_values(0)
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    delta = df['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.ewm(span=14, adjust=False).mean()
    avg_loss = loss.ewm(span=14, adjust=False).mean()
    RS = avg_gain / avg_loss
    df['RSI_14'] = 100 - (100 / (1 + RS))
    return df


# --- 2. STREAMLIT UI LAYOUT ---

st.set_page_config(
    page_title="Pandas Stock Analysis Dashboard",
    layout="wide"
)

st.title("Interactive Stock Time Series Analysis")
st.markdown("Powered by Pandas, yfinance, and Streamlit.")

# --- Sidebar for User Input ---
st.sidebar.header("Stock and Date Selection")
ticker_symbol = st.sidebar.text_input("Ticker Symbol (e.g., AAPL)", value='MSFT')
start = st.sidebar.date_input("Start Date", value=pd.to_datetime('2021-01-01'))
end = st.sidebar.date_input("End Date", value=date.today())
show_sma = st.sidebar.checkbox("Show 50-Day SMA", value=True)
show_ema = st.sidebar.checkbox("Show 20-Day EMA", value=True)

# --- Main App Logic ---

if ticker_symbol:
    # Fetch and Analyze Data
    data = get_analyzed_data(ticker_symbol, start, end)

    if data is not None:
        st.subheader(f"Analysis for {ticker_symbol.upper()}")
        
        # --- A. Price and Trend Chart ---
        st.markdown("### Price and Trend")
        plot_cols = ['Close']
        if show_sma: plot_cols.append('SMA_50')
        if show_ema: plot_cols.append('EMA_20')
        
        st.line_chart(data[plot_cols])
        
        # --- B. Key Metrics (from Notebook 10) ---
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Calculate Total Return (Simplified from Notebook 04)
            total_return = (data['Close'].iloc[-1] / data['Close'].iloc[0]) - 1
            st.metric("Total Return", f"{total_return:.2%}")
            
        with col2:
            # Get Last RSI Value
            last_rsi = data['RSI_14'].iloc[-1]
            st.metric("Current 14-Day RSI", f"{last_rsi:.2f}")
            
        with col3:
            # Calculate Volatility (Annualized from Daily Log Returns)
            data['Log_Return'] = np.log(data['Close']).diff()
            annualized_vol = data['Log_Return'].std() * np.sqrt(252)
            st.metric("Annualized Volatility", f"{annualized_vol:.2%}")
            
        # --- C. Momentum Chart (RSI) ---
        st.markdown("### Momentum (RSI)")
        st.line_chart(data['RSI_14'])
        st.markdown("\*Note: RSI above 70 is overbought, below 30 is oversold.")

    else:
        st.error("Could not retrieve data for this ticker/date range.")


# End of app.py script