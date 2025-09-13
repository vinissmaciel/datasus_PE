import pandas as pd

# List of CSV file paths
csv_files = [
    '../2019.csv',
    '../2020.csv',
    '../2021.csv',
    '../2022.csv',
    '../2023.csv',
    '../2024.csv',
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
