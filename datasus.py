import pandas as pd

# List of CSV file paths
csv_files = [
    'data/2019.csv',
    'data/2020.csv',
    'data/2021.csv',
    'data/2022.csv',
    'data/2023.csv',
    'data/2024.csv',
]

# Initialize an empty list to store dataframes
dfs = []

# Loop through each CSV file, read it into a dataframe, and append to the list
for file in csv_files:
    df = pd.read_csv(file, encoding='latin1', low_memory=False)
    dfs.append(df)

# Concatenate all dataframes into a single dataframe
combined_df = pd.concat(dfs, ignore_index=True)

# Display the first few rows of the combined dataframe and its information
print("Combined DataFrame Head:")
print(combined_df.head())
print("\nCombined DataFrame Info:")
combined_df.info()
combined_df.to_csv("combined_data.csv", index=False, encoding="utf-8")
