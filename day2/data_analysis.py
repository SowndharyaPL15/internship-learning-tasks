import numpy as np
import pandas as pd

# 1. NumPy array operations
marks = np.array([85, 92, 76, 89, 68])

print("=== NUMPY OPERATIONS ===")
print("Marks:", marks)
print("Average marks:", np.mean(marks))
print("Highest marks:", np.max(marks))
print("Marks after adding 5:", marks + 5)

# 2. Load CSV data into a pandas DataFrame
data = pd.read_csv("day2/students.csv")

print("\n=== FIRST FIVE RECORDS ===")
print(data.head())

# 3. Inspect the dataset
print("\n=== DATASET INFORMATION ===")
data.info()

print("\n=== STATISTICAL SUMMARY ===")
print(data.describe())

# 4. Handle missing values
print("\n=== MISSING VALUES ===")
print(data.isnull().sum())

# 5. Filter students with Python marks above 80
high_scorers = data[data["python"] > 80]

print("\n=== STUDENTS SCORING ABOVE 80 IN PYTHON ===")
print(high_scorers[["name", "python"]])

# 6. Calculate average marks for each subject
print("\n=== SUBJECT AVERAGES ===")
print(data[["python", "sql", "communication"]].mean())

# 7. Add a total marks column
data["total"] = data[["python", "sql", "communication"]].sum(axis=1)

print("\n=== TOTAL MARKS ===")
print(data[["name", "total"]])

# 8. Save the analyzed data
data.to_csv("day2/student_analysis.csv", index=False)

print("\nAnalysis completed. Results saved to day2/student_analysis.csv")
