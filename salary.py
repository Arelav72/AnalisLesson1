import pandas as pd

df = pd.read_csv('dz.csv')
#print(df.head())
#print(df.tail())

group = df.groupby('City')['Salary'].mean()
print(group)