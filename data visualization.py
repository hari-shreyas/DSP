import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_name = "titanic.csv"  # Replace with "data.csv" or "salary.csv" as needed
data = pd.read_csv(file_name)

# Display the first few rows to understand the structure of the data
print("Data Preview:")
print(data.head())

# Visualizations
plt.figure(figsize=(12, 8))

# 1. Countplot of a categorical column (e.g., gender or class in Titanic)
if "Sex" in data.columns:  # Adjust column name based on your CSV
    plt.subplot(2, 2, 1)
    sns.countplot(x="Sex", data=data, palette="viridis")
    plt.title("Count of Gender")

# 2. Histogram of a numerical column (e.g., age or salary)
if "Age" in data.columns:  # Adjust column name based on your CSV
    plt.subplot(2, 2, 2)
    sns.histplot(data["Age"].dropna(), kde=True, bins=30, color="blue")
    plt.title("Age Distribution")

# 3. Boxplot to check distribution (e.g., Fare in Titanic, Salary in salary.csv)
if "Fare" in data.columns:  # Adjust column name based on your CSV
    plt.subplot(2, 2, 3)
    sns.boxplot(x=data["Fare"], color="green")
    plt.title("Fare Distribution")

# 4. Heatmap for correlation between numerical features
if data.select_dtypes(include=['float64', 'int64']).shape[1] > 1:  # Check if numerical data exists
    plt.subplot(2, 2, 4)
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()
