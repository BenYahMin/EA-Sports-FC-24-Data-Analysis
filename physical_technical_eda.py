import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
filepath = r"C:\Users\benja\Documents\Main\EA Sports FC 24\Datasets\male_players.csv"
df_male = pd.read_csv(filepath, low_memory=False)

# Extract the primary position (the first position listed)
df_male['primary_position'] = df_male['player_positions'].astype(str).apply(lambda x: x.split(',')[0].strip())

# Filter for just Center Backs (CB) and Strikers (ST)
df_pos = df_male[df_male['primary_position'].isin(['CB', 'ST'])].copy()

# The 6 main attribute categories in FIFA
attributes = ['pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']

# Drop rows where these attributes might be missing (like Goalkeepers, though we filtered for CB/ST)
df_pos = df_pos.dropna(subset=attributes)

# Calculate the mean for each attribute by position
pos_means = df_pos.groupby('primary_position')[attributes].mean().reset_index()

# Melt the dataframe so it's easier to plot with seaborn
pos_melted = pd.melt(pos_means, id_vars=['primary_position'], value_vars=attributes, 
                     var_name='Attribute', value_name='Average Rating')

# Set up the visualization
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# Create a grouped bar chart
barplot = sns.barplot(
    data=pos_melted, 
    x='Attribute', 
    y='Average Rating', 
    hue='primary_position', 
    palette={'CB': '#1f77b4', 'ST': '#d62728'}
)

plt.title('Attribute Comparison: Center Backs (CB) vs. Strikers (ST)', fontsize=14, fontweight='bold')
plt.xlabel('Player Attribute', fontsize=12)
plt.ylabel('Average Rating', fontsize=12)
plt.legend(title='Position')
plt.ylim(20, 80) # Set y-limit for better visual scaling

# Add values on top of bars
for p in barplot.patches:
    barplot.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points')

plt.tight_layout()
plt.savefig('attributes_comparison.png', dpi=300)
plt.show()

print("--- Mean Attributes by Position ---")
print(pos_means.to_string(index=False))