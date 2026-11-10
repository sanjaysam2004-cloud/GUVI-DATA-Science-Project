import streamlit as st
import pandas as pd

st.set_page_config(page_title="NYC 311 Dashboard", layout="wide")

st.title("NYC 311 Complaint Analysis Dashboard")

df = pd.read_csv("cleaned_311_data.csv")

st.success("Data loaded successfully!")

st.metric("Total Complaints", len(df))

st.subheader("Complaint Type Analysis")

if "complaint_type" in df.columns:
    complaint_counts = df["complaint_type"].value_counts()
    st.bar_chart(complaint_counts.head(10))

st.subheader("Borough Analysis")

if "borough" in df.columns:
    borough_counts = df["borough"].value_counts()
    st.bar_chart(borough_counts)

st.subheader("Status Analysis")

if "status" in df.columns:
    status_counts = df["status"].value_counts()
    st.bar_chart(status_counts)

st.write("Dashboard completed successfully!")