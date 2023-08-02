import pandas as pd
import matplotlib.pyplot as plt

# Reading the data (assuming you have a CSV file with player data)
data = pd.read_csv('/Users/jeremycarter/Downloads/PPAD.csv')


print(data.columns)

# Remove non-numeric characters from 'COST' column
data['COST'] = data['COST'].str.replace('$', '').astype(float)

# Convert 'FPTS' column to numeric
data['FPTS'] = pd.to_numeric(data['FPTS'], errors='coerce')

# Filter out players with cost less than $1
data = data[data['COST'] >= 1]

# Calculate fantasy points per cost (FPC) for each player
data['FPC'] = data['FPTS'] / data['COST']

# Calculate the average fantasy points for each position
average_fpts_by_position = data.groupby('Position')['FPTS'].mean()

# Calculate the VBD for each player
data['VBD'] = data.apply(lambda row: row['FPTS'] - average_fpts_by_position[row['POSITION']], axis=1)

# Sort the DataFrame based on VBD to identify players with higher relative value
data_sorted_by_vbd = data.sort_values(by='VBD', ascending=False)

# Find the players within the optimal cost range (e.g., between $1 and $10)
optimal_range = data_sorted_by_vbd[(data_sorted_by_vbd['COST'] >= 1) & (data_sorted_by_vbd['COST'] <= 10)]

# Print the players within the optimal cost range
print("Players within the optimal cost range:")
print(optimal_range)

# Scatter plot
data.plot(x='COST', y='FPTS', kind='scatter', figsize=(10, 6))
plt.title('Cost over Fantasy Points')
plt.xlabel('COST')
plt.ylabel('FPTS')

# Adding player labels for players within the optimal cost range
for _, row in optimal_range.iterrows():
    plt.annotate(row['PLAYER'], (row['COST'], row['FPTS']), xytext=(5, 5), textcoords='offset points')

plt.show()