import streamlit as st
import pandas as pd

st.set_page_config(page_title="Insightify Dashboard", layout="wide")

st.title("📊 Insightify - Data Analytics Dashboard")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📌 Data Preview")
    st.dataframe(df)

    st.subheader("📊 Summary Statistics")
    st.write(df.describe())

    column = st.selectbox("Select column for visualization", df.columns)

    st.subheader("📈 Visualizations")
    st.line_chart(df[column])
    st.bar_chart(df[column])

    if st.checkbox("Show Pie Chart"):
        st.write(df[column].value_counts().plot.pie(autopct='%1.1f%%'))
        st.pyplot()
