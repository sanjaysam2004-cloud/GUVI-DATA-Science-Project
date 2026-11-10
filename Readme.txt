NYC 311 COMPLAINT DATA ANALYSIS

1. Project Introduction

This project focuses on analyzing NYC 311 complaint data using Data Science techniques.

The main purpose is to understand complaint patterns, identify frequently reported issues, analyze complaint status, and study resolution trends.

2. Project Objectives

- Analyze NYC 311 complaint records.
- Identify the most common complaint types.
- Analyze complaints by borough.
- Study complaint status.
- Visualize daily and monthly complaint trends.
- Build an interactive dashboard.

3. Tools and Technologies

1. Python
2. Pandas
3. Matplotlib
4. MySQL
5. Streamlit
6. Jupyter / PowerShell

4. Dataset Description

The dataset used in this project is NYC 311 Complaint Data.

The dataset contains approximately 99,998 cleaned complaint records.

Dataset Columns

1. Unique Key – Unique complaint identification number.
2. Created Date – Date and time when complaint was created.
3. Closed Date – Date and time when complaint was closed.
4. Agency – Department responsible for the complaint.
5. Complaint Type – Type of complaint reported.
6. Descriptor – Detailed description of the complaint.
7. Borough – Location of the complaint.
8. Status – Current complaint status.
9. Latitude – Geographic latitude.
10. Longitude – Geographic longitude.
11. Resolution Hours – Calculated complaint resolution time.

Data Cleaning

- Checked missing values.
- Removed duplicate records.
- Converted date columns.
- Created resolution hours.
- Saved cleaned data as CSV.

5. Data Analysis and Visualization

Data analysis was performed using Python, Pandas, and MySQL.

Analysis Performed

1. Total complaint count analysis.
2. Complaint type analysis.
3. Borough-wise complaint analysis.
4. Status-wise complaint analysis.
5. Resolution time analysis.
6. Daily complaint trend analysis.
7. Monthly complaint trend analysis.
8. Outlier analysis using IQR method.

Visualizations Created

- Top 10 Complaint Types Bar Chart
- Borough-wise Complaint Chart
- Status Analysis Chart
- Daily Complaint Trend Line Chart
- Monthly Complaint Trend Bar Chart
- Resolution Time Chart
- Correlation Heatmap

These visualizations help understand complaint patterns and trends.

6. MySQL Analysis

MySQL was used to perform structured queries and analyze the cleaned NYC 311 complaint dataset.

SQL Analysis Performed

1. Total number of complaints.
2. Complaint status count.
3. Borough-wise complaint count.
4. Top 10 complaint types.
5. Average resolution time.
6. Minimum and maximum resolution time.
7. Daily and monthly complaint analysis.
8. Status-wise complaint analysis.
9. Duplicate record checking.
10. Missing value checking.
11. IQR-based outlier analysis.

Result

SQL queries helped identify complaint patterns, borough-wise distribution, complaint status, and resolution time statistics.

7. Streamlit Dashboard

An interactive dashboard was developed using Streamlit to explore the cleaned NYC 311 complaint data.

Dashboard Features

- KPI cards for total, filtered, and closed complaints.
- Borough filter.
- Complaint status filter.
- Complaint type filter.
- Start and end date filters.
- Daily complaint trend line chart.
- Monthly complaint trend bar chart.
- Download option for filtered records as CSV.

The dashboard allows users to interactively explore complaint patterns and download selected data.

8. Conclusion

This project demonstrates how Python, Pandas, MySQL, and Streamlit can be used to clean, analyze, and visualize NYC 311 complaint data.

The interactive dashboard helps users explore complaint patterns based on borough, complaint type, status, and date.

This project improved practical knowledge of data cleaning, SQL queries, data visualization, and dashboard development.