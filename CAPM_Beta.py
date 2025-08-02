import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objs as go

st.set_page_config(page_title="CAPM Beta & Return", layout="wide")

st.markdown("<h1 style='font-weight:bold;'>Calculate Beta and Return for Individual Stock</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    stock = st.text_input("Choose a stock", value="TSLA")
with col2:
    years = st.number_input("Number of Years", min_value=1, max_value=10, value=1, step=1)

benchmark = "^GSPC"  # S&P 500
period = f"{years}y"

# Fetch stock and benchmark data
df_stock_raw = yf.download(stock, period=period, interval="1wk")
df_bench_raw = yf.download(benchmark, period=period, interval="1wk")

# Handle 'Adj Close' fallback
if 'Adj Close' in df_stock_raw.columns:
    df_stock = df_stock_raw['Adj Close']
elif 'Close' in df_stock_raw.columns:
    df_stock = df_stock_raw['Close']
else:
    df_stock = pd.Series(dtype=float)

if 'Adj Close' in df_bench_raw.columns:
    df_bench = df_bench_raw['Adj Close']
elif 'Close' in df_bench_raw.columns:
    df_bench = df_bench_raw['Close']
else:
    df_bench = pd.Series(dtype=float)

# Error if data not found
if df_stock.empty or df_bench.empty:
    st.error("Data not available for the selected stock or benchmark. Please try another ticker.")
else:
    # Combine and clean data
    df = pd.concat([df_stock, df_bench], axis=1)
    df.columns = [stock, "Benchmark"]
    df = df.dropna()

    # Calculate weekly returns
    returns = df.pct_change().dropna() * 100

    # Beta calculation using linear regression
    beta, alpha = np.polyfit(returns["Benchmark"], returns[stock], 1)

    # Annualized return
    avg_return = returns[stock].mean() * 52  # Weekly to yearly

    # Display metrics
    st.markdown(f"<h3>Beta : {beta:.4f}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3>Annual Return : {avg_return:.2f}%</h3>", unsafe_allow_html=True)

    # Scatter plot with regression line
    scatter = go.Scatter(
        x=returns["Benchmark"],
        y=returns[stock],
        mode='markers',
        name=stock,
        marker=dict(color='skyblue', size=8, opacity=0.7)
    )
    reg_line = go.Scatter(
        x=returns["Benchmark"],
        y=beta * returns["Benchmark"] + alpha,
        mode='lines',
        name='Regression Line',
        line=dict(color='red')
    )

    layout = go.Layout(
        title=f"{stock} vs Benchmark",
        xaxis=dict(title='Benchmark Returns (%)'),
        yaxis=dict(title=f'{stock} Returns (%)'),
        showlegend=False,
        height=500,
    )

    fig = go.Figure(data=[scatter, reg_line], layout=layout)
    st.plotly_chart(fig, use_container_width=True)
