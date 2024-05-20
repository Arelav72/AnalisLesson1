import pandas as pd

df = pd.read_csv('Financial Allocations.csv')
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())