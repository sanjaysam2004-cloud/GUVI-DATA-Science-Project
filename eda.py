import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_311_data.csv")

print("Dataset Shape:", df.shape)

print("\nTop 10 Complaint Types:")
print(df["complaint_type"].value_counts().head(10))

# Borough-wise Complaints

borough_counts = df["borough"].value_counts()

plt.figure(figsize=(10, 5))
borough_counts.plot(kind="bar")

plt.title("Complaints by Borough")
plt.xlabel("Borough")
plt.ylabel("Number of Complaints")

plt.tight_layout()
plt.savefig("borough_complaints.png")
plt.show()
# Agency-wise Complaints

agency_counts = df["agency"].value_counts()

print("\nAgency-wise Complaints:")
print(agency_counts)
# Resolution Time Analysis

df["created_date"] = pd.to_datetime(df["created_date"])
df["closed_date"] = pd.to_datetime(df["closed_date"])

df["resolution_hours"] = (
    df["closed_date"] - df["created_date"]
).dt.total_seconds() / 3600

print("\nAverage Resolution Time:")
print(df["resolution_hours"].mean())
print("\nAverage Resolution Time:")
print(df["resolution_hours"].mean())
# Resolution Time Graph

plt.figure(figsize=(8, 5))
df["resolution_hours"].dropna().plot(kind="hist", bins=30)

plt.title("Distribution of Resolution Time")
plt.xlabel("Resolution Time (Hours)")
plt.ylabel("Number of Complaints")

plt.tight_layout()
plt.savefig("resolution_time.png")
plt.show()
# Top 10 Complaint Types Graph

top_complaints = df["complaint_type"].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_complaints.plot(kind="bar")

plt.title("Top 10 Complaint Types")
plt.xlabel("Complaint Type")
plt.ylabel("Number of Complaints")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("top_complaints.png")
plt.show()
# Monthly Complaint Trend

df["created_date"] = pd.to_datetime(df["created_date"])

monthly_counts = df.groupby(
    df["created_date"].dt.to_period("M")
).size()

print("\nMonthly Complaints:")
print(monthly_counts)

monthly_counts.plot(kind="line", marker="o")

plt.title("Monthly Complaint Trend")
plt.xlabel("Month")
plt.ylabel("Number of Complaints")

plt.tight_layout()
plt.savefig("monthly_trend.png")
plt.show()
# Complaint Status Analysis

status_counts = df["status"].value_counts()

print("\nComplaint Status:")
print(status_counts)

plt.figure(figsize=(8, 5))
status_counts.plot(kind="bar")

plt.title("Complaint Status Analysis")
plt.xlabel("Status")
plt.ylabel("Number of Complaints")

plt.tight_layout()
plt.savefig("status_analysis.png")
plt.show()
# Missing Values Analysis

print("\nMissing Values:")
print(df.isnull().sum())

missing_values = df.isnull().sum()
missing_values = missing_values[missing_values > 0]

missing_values.plot(kind="bar", figsize=(10, 5))

plt.title("Missing Values Analysis")
plt.xlabel("Columns")
plt.ylabel("Missing Count")

plt.tight_layout()
plt.savefig("missing_values.png")
plt.show()
# Correlation Analysis

numeric_df = df.select_dtypes(include="number")

correlation = numeric_df.corr()

print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(10, 6))
plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()

plt.xticks(range(len(correlation.columns)),
correlation.columns, rotation=45)

plt.yticks(range(len(correlation.columns)), 
correlation.columns)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()
# Final EDA Summary

print("\n========== FINAL EDA SUMMARY ==========")

print("Total Complaints:", len(df))
print("Top Complaint Type:", df["complaint_type"].value_counts().idxmax())
print("Top Borough:", df["borough"].value_counts().idxmax())
print("Most Common Status:", df["status"].value_counts().idxmax())
print("Average Resolution Time:",
      round(df["resolution_hours"].mean(), 2), "Hours")

print("=======================================")
# Extract Time Buckets

df["created_date"] = pd.to_datetime(df["created_date"], errors="coerce")

df["created_year"] = df["created_date"].dt.year
df["created_month"] = df["created_date"].dt.month
df["created_weekday"] = df["created_date"].dt.day_name()
df["created_hour"] = df["created_date"].dt.hour

df.to_csv("cleaned_311_data.csv", index=False)

print("\nTime Buckets Created Successfully!")
print(df[["created_year", "created_month", "created_weekday", "created_hour"]].head())