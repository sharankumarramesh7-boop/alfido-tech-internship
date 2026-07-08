import pandas as pd

try:
    # Load the CSV dataset
    df = pd.read_csv("sample_dataset.csv")

    # Display the first five rows
    print("First Five Rows:")
    print(df.head())

    # Display dataset information
    print("\nDataset Information:")
    print(df.info())

    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Fill missing salary values with the average salary
    df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Filter employees with salary greater than 50000
    high_salary = df[df["Salary"] > 50000]

    print("\nEmployees with Salary greater than 50000:")
    print(high_salary)

    # Group by Department and calculate average salary
    print("\nAverage Salary by Department:")
    print(df.groupby("Department")["Salary"].mean())

except FileNotFoundError:
    print("Error: sample_dataset.csv not found.")

except Exception as e:
    print("An error occurred:", e)
