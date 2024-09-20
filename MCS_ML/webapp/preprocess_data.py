import pandas as pd
from sklearn.preprocessing import StandardScaler

# Dataset location specified properly
data = pd.read_csv('../data/simulated_malware_dataset.csv')

data.dropna(inplace=True)

# Only numeric data needed.
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
data_numeric = data[numeric_columns]

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data_numeric)

data[numeric_columns] = scaled_data

data.to_csv('../data/simulated_malware_dataset.csv', index=False)
# Saved and replaced
# Nothing to export here
