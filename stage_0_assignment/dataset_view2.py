import pandas as pd

data = 'iris.csv'
df = pd.read_csv(data)

summary_stats = df.describe()
print(summary_stats)
