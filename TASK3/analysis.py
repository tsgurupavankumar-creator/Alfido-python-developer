import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Show first 5 rows
print("FIRST 5 ROWS")
print(df.head())

# Dataset info
print("\nDATASET INFO")
print(df.info())

# Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Statistics
print("\nSTATISTICS")
print(df.describe())

# Example filtering
print("filtering")
filtered = df[df["age"] < 20]
print(filtered)

# Example grouping
print("grouping")
grouped = df.groupby("age")["sleep_hours"].mean()
print(grouped)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\nData cleaned successfully!")