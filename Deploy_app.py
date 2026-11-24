import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="GDP Dashboard", layout="wide")
st.title("🌍 GDP Dashboard")
st.write("GDP comparison of countries")

data = {
    "Country": ["USA", "China", "Japan", "Germany", "India", "UK", "France", "Pakistan"],
    "GDP (Trillion USD)": [27.36, 17.79, 4.23, 4.45, 3.73, 3.34, 3.05, 0.34]
}
df = pd.DataFrame(data)

country = st.multiselect("Select Country", df["Country"].unique(), default=df["Country"].unique())
filtered = df[df["Country"].isin(country)]

col1, col2 = st.columns(2)
with col1:
    st.subheader("GDP Data")
    st.dataframe(filtered)
with col2:
    st.subheader("GDP Chart")
    fig = px.bar(filtered, x="Country", y="GDP (Trillion USD)", color="Country", title="GDP by Country")
    st.plotly_chart(fig, use_container_width=True)

st.success("Dashboard deployed successfully!")
