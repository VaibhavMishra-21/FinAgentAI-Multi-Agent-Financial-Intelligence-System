import streamlit as st
import plotly.express as px

from services.yahoo_finance import YahooFinanceService

st.title("FinAgentAI")

symbol = st.text_input("Stock Symbol", "AAPL")

data = YahooFinanceService.get_stock_data(symbol)

st.subheader("Stock Data")

fig = px.line(
    data,
    y="Close",
    title=f"{symbol} Closing Price"
)

st.plotly_chart(fig)
