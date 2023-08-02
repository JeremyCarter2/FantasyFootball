import pandas as pd
import matplotlib.pyplot as plt

# Reading the data
data = pd.read_csv('/Users/jeremycarter/Downloads/PPAD.csv')

# print(data.columns)

# Remove non-numeric characters from 'COST' column
data['COST'] = data['COST'].str.replace('$', '').astype(float)

# Convert to numeric
data['FPTS'] = pd.to_numeric(data['FPTS'])


# Scatter plot
data.plot(x='COST', y='FPTS', kind='scatter', figsize=(10, 6))
plt.title('Cost over Fantasy Points')
plt.xlabel('COST')
plt.ylabel('FPTS')

# Adding player labels

for _, row in data.iterrows():
    plt.annotate(row['PLAYER'], (row['COST'], row['FPTS']), xytext=(5,5), textcoords='offset points')

plt.show()