import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# 5 Attributes
print("\nAttributes:")
print(f"1. Shape of DataFrame: {df.shape}")  # Number of rows and columns
print(f"2. Columns in DataFrame: {df.columns}")  # List of column names
print(f"3. Index of DataFrame: {df.index}")  # Index of the DataFrame
print(f"4. Data types of each column: {df.dtypes}")  # Data types of columns
print(f"5. Size of DataFrame: {df.size}")  # Total number of elements

# 5 Methods
print("\nMethods:")
print("1. Head of the DataFrame:")
print(df.head(2))  # Displays the first 2 rows

print("\n2. Describe the DataFrame:")
print(df.describe())  # Summary statistics for numerical columns

print("\n3. Transpose the DataFrame:")
print(df.T)  # Transpose rows and columns

print("\n4. Sort the DataFrame by 'Age':")
print(df.sort_values("Age"))  # Sort by Age column

print("\n5. Filter rows where Age > 30:")
print(df[df["Age"] > 30])  # Filter rows based on a condition