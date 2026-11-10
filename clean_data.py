import pandas as pd

df = pd.read_csv("raw_311_data.csv")

print("Original Shape:", df.shape)

print(df.head())

print("Missing Values:")
print(df.isnull().sum())

print("Duplicate Records:")
print(df.duplicated().sum())
date_columns = ["created_date", "closed_date"]

for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

print("Date conversion completed!")

print(df[date_columns].dtypes)
df["resolution_hours"] = (
    df["closed_date"] - df["created_date"]
).dt.total_seconds() / 3600

print("Resolution Hours Calculated!")

print(df[["created_date", "closed_date", "resolution_hours"]].head())
print("Missing Values After Date Conversion:")
print(df.isnull().sum())
print("Duplicate Records:")
print(df.duplicated().sum())
print("Duplicates Removed!")
print("New Shape:", df.shape)
df["missing_location"] = df["latitude"].isnull() | df["longitude"].isnull()

df["missing_closed_date"] = df["closed_date"].isnull()

print("Data Quality Check Completed!")
print(df[["missing_location", "missing_closed_date"]].head())
df.to_csv("cleaned_311_data.csv", index=False)

print("Cleaned Data Saved Successfully!")
print("Final Shape:", df.shape)
print("Total Records:", len(df))
print("Total Columns:", len(df.columns))
print("Final Shape:", df.shape)
print("Total Records:", len(df))
print("Total Columns:", len(df.columns))
df = df.drop_duplicates()

print("Remaining Duplicates:", df.duplicated().sum())
df.to_csv("cleaned_311_data.csv", index=False)

print("Cleaned Data Saved Successfully!")

