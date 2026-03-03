import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("task1_dataset1.csv")

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Info about data
print("\nDataset Info:")
print(df.info())

# Count authors
author_count = df['Author'].value_counts()
print("\nAuthor Count:")
print(author_count)

# Plot graph
author_count.plot(kind='bar')
plt.title("Number of Quotes per Author")
plt.xlabel("Author")
plt.ylabel("Count")
plt.show()