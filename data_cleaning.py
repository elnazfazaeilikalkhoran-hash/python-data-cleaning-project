import pandas as pd

# Load the dataset
df = pd.read_csv("sample_dataset.csv")

# Display basic information
print("Original dataset:")
print(df.head())
print("\nDataset information:")
print(df.info())

# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Rename columns to lowercase
df.columns = df.columns.str.lower()

# Fill missing values
df["age"] = df["age"].fillna(df["age"].mean())
df["score"] = df["score"].fillna(df["score"].mean())
df["city"] = df["city"].fillna("Unknown")
df["email"] = df["email"].fillna("Not provided")

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nCleaned dataset saved as cleaned_dataset.csv")
