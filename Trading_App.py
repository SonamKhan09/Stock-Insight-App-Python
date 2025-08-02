import streamlit as st
st.set_page_config(
  page_title = "Trading App",
  page_icon = "chart_with_downwards_trend:",
  layout = "wide"
)

st.title("Trading Guide App :bar_chart:")

st.header("We provide the Greatest platform for you to collect all information prior to investing in stocks.")

st.image("app.jpg", use_column_width=True)

st.markdown("## We provide the following services:")

st.markdown("#### :one: Stock Information")
st.write("Through this page, you can see the latest stock prices, historical data, and market trends.")

st.markdown("#### :two: Stock Predictions")
st.write("you can explore predicted closing prices for the next 30 days based on historical data and market trends. Use advanced forecasting techniques to make informed investment decisions.")

st.markdown("#### :three: CAPM Return")
st.write("Discover the expected return of a stock using the Capital Asset Pricing Model (CAPM). This tool helps you understand the relationship between risk and return, enabling you to make better investment choices.")

st.markdown("#### :four: CAPM Beta")
st.write("Calculate the beta of a stock, which measures its volatility compared to the market. This information is crucial for assessing risk and making informed investment decisions.")