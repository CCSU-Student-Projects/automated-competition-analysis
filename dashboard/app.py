import sqlite3
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

from analysis.metrics import add_growth_metrics

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "aca.db"

st.set_page_config(page_title="ACA Dashboard", layout="wide")
st.title("Automated Competition Analysis Pipeline")

if not DB_PATH.exists():
    st.error("Database not found. Run: python -m etl.pipeline_runner")
    st.stop()

conn = sqlite3.connect(DB_PATH)
df = pd.read_sql("SELECT * FROM stock_prices", conn)
conn.close()

df["date"] = pd.to_datetime(df["date"])
df = add_growth_metrics(df)

st.subheader("Stock Price History")
fig = px.line(df, x="date", y="close", color="symbol", title="Closing Price Over Time")
st.plotly_chart(fig, use_container_width=True)

latest_close = df.iloc[-1]["close"]
latest_pct = df.iloc[-1]["daily_pct_change"]

col1, col2 = st.columns(2)
col1.metric("Latest Close", f"{latest_close:.2f}")
col2.metric("Daily % Change", f"{latest_pct:.2f}%")

st.subheader("Recent Data")
st.dataframe(df.tail(10))