import streamlit as st
import requests
import pandas as pd

# Base API URL
BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="📊 Social Pulse Analyzer", layout="wide")
st.title("📊 Social Pulse Analyzer Dashboard")

# 🔁 Reload Data Button
if st.button("🔄 Load Dashboard Summary"):
    response = requests.get(f"{BASE_URL}/dashboard-summary")
    if response.status_code == 200:
        data = response.json()
        st.success("Data loaded successfully!")
        st.metric("Total Posts", data["total_posts"])
        st.metric("Avg. Engagement Rate", data["avg_engagement_rate"])
        st.write(f"📅 Date Range: {data['date_range']}")
    else:
        st.error("Failed to fetch summary!")

# 📌 Top Posts
st.header("🔝 Top Engaging Posts")
top_n = st.slider("Select how many posts to view", 5, 20, 10)
response = requests.get(f"{BASE_URL}/top-posts?limit={top_n}")
if response.status_code == 200:
    df_top = pd.DataFrame(response.json())
    st.dataframe(df_top)
else:
    st.warning("Couldn't fetch top posts")

# 📊 Engagement by Platform
st.header("📊 Engagement by Platform")
response = requests.get(f"{BASE_URL}/engagement-by-platform")
if response.status_code == 200:
    df_platform = pd.DataFrame(response.json())
    st.bar_chart(df_platform.set_index("platform"))
else:
    st.warning("Couldn't fetch platform data")

# 🕒 Engagement by Time Unit
st.header("🕒 Engagement by Time")
time_unit = st.selectbox("Select time unit", ["day_of_week", "hour_of_day", "month"])
response = requests.get(f"{BASE_URL}/engagement-by-time?time_unit={time_unit}")
if response.status_code == 200:
    df_time = pd.DataFrame(response.json())
    st.bar_chart(df_time.set_index(time_unit))
else:
    st.warning("Couldn't fetch time data")
