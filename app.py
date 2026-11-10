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
st.sidebar.header("Dashboard Filters")

borough_list = ["All"] + sorted(df["borough"].dropna().unique().tolist())

selected_borough = st.sidebar.selectbox(
    "Select Borough",
    borough_list
)

if selected_borough != "All":
    filtered_df = df[df["borough"] == selected_borough]
else:
    filtered_df = df.copy()

st.subheader("Filtered Complaints")
st.metric("Selected Borough Complaints", len(filtered_df))

st.bar_chart(filtered_df["complaint_type"].value_counts().head(10))
status_list = ["All"] + sorted(df["status"].dropna().unique().tolist())

selected_status = st.sidebar.selectbox(
    "Select Status",
    status_list
)

if selected_status != "All":
    filtered_df = filtered_df[
        filtered_df["status"] == selected_status
    ]

st.metric("Filtered Total Complaints", len(filtered_df))
complaint_list = ["All"] + sorted(
    df["complaint_type"].dropna().unique().tolist()
)

selected_complaint = st.sidebar.selectbox(
    "Select Complaint Type",
    complaint_list
)

if selected_complaint != "All":
    filtered_df = filtered_df[
        filtered_df["complaint_type"] == selected_complaint
    ]

st.metric("Final Filtered Complaints", len(filtered_df))
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Complaints", len(df))

with col2:
    st.metric("Filtered Complaints", len(filtered_df))

with col3:
    closed_count = len(filtered_df[filtered_df["status"] == "Closed"])
    st.metric("Closed Complaints", closed_count)
csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Data",
    data=csv_data,
    file_name="filtered_311_data.csv",
    mime="text/csv"
)
st.sidebar.header("Date Filter")

df["created_date"] = pd.to_datetime(df["created_date"])

min_date = df["created_date"].min().date()
max_date = df["created_date"].max().date()

start_date = st.sidebar.date_input(
    "Start Date",
    min_date,
    min_value=min_date,
    max_value=max_date
)

end_date = st.sidebar.date_input(
    "End Date",
    max_date,
    min_value=min_date,
    max_value=max_date
)

filtered_df = filtered_df[
    (pd.to_datetime(filtered_df["created_date"]).dt.date >= start_date) &
    (pd.to_datetime(filtered_df["created_date"]).dt.date <= end_date)
]

st.metric("Date Filtered Complaints", len(filtered_df))
st.subheader("Daily Complaint Trend")
daily_dates = pd.to_datetime(
    filtered_df["created_date"],
    errors="coerce"
)

daily_trend = daily_dates.dt.date.value_counts().sort_index()

st.line_chart(daily_trend)
st.subheader("Monthly Complaint Trend")

monthly_dates = pd.to_datetime(
    filtered_df["created_date"],
    errors="coerce"
)

monthly_trend = (
    monthly_dates.dropna()
    .dt.to_period("M")
    .astype(str)
    .value_counts()
    .sort_index()
)

st.bar_chart(monthly_trend)



st.line_chart(daily_trend)

 