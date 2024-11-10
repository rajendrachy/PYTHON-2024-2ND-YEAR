import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Adding a new column
df['Salary'] = [70000, 80000, 120000, 110000]

# Display the updated DataFrame
print("\nUpdated DataFrame:")
print(df)

# Basic operations
average_age = df['Age'].mean()
print("\nAverage Age:", average_age)

# Filtering data
older_than_30 = df[df['Age'] > 30]
print("\nPeople older than 30:")
print(older_than_30)

# Sorting data
sorted_df = df.sort_values(by='Salary', ascending=False)
print("\nDataFrame sorted by Salary (Descending):")
print(sorted_df)

# Saving to a CSV file
df.to_csv('data.csv', index=False)
