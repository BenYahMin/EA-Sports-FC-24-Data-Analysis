import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the datasets
male_filepath = r"C:\Users\benja\Documents\Main\EA Sports FC 24\Datasets\male_players.csv"
female_filepath = r"C:\Users\benja\Documents\Main\EA Sports FC 24\Datasets\female_players.csv"
df_male = pd.read_csv(male_filepath, low_memory=False)
df_female = pd.read_csv(female_filepath, low_memory=False)

# Add a Gender column
df_male['Gender'] = 'Male'
df_female['Gender'] = 'Female'

# Select relevant columns for comparison
cols = ['Gender', 'overall', 'pace', 'physic', 'shooting', 'passing', 'dribbling', 'defending', 'height_cm', 'weight_kg']

# Combine datasets for these columns
df_combined = pd.concat([df_male[cols], df_female[cols]], ignore_index=True)
df_combined = df_combined.dropna()

# 1. Calculate Summary Statistics
summary_stats = df_combined.groupby('Gender')[['overall', 'pace', 'physic', 'height_cm', 'weight_kg']].mean().round(1)

# 2. Visualizations
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Gender Parity: Comparing Attribute Distributions', fontsize=16, fontweight='bold')

# Plot A: Overall Rating Distribution (KDE)
sns.kdeplot(data=df_combined, x='overall', hue='Gender', fill=True, common_norm=False, ax=axes[0, 0], palette={'Male': '#1f77b4', 'Female': '#e377c2'})
axes[0, 0].set_title('Distribution of Overall Ratings')
axes[0, 0].set_xlabel('Overall Rating')

# Plot B: Pace vs Physic (Scatter sample to avoid overplotting)
# Taking a random sample of 5000 males to match the female dataset size for a fair visual comparison
df_male_sample = df_combined[df_combined['Gender'] == 'Male'].sample(n=len(df_female), random_state=42)
df_female_only = df_combined[df_combined['Gender'] == 'Female']
df_scatter = pd.concat([df_male_sample, df_female_only])

sns.scatterplot(data=df_scatter, x='physic', y='pace', hue='Gender', alpha=0.3, ax=axes[0, 1], palette={'Male': '#1f77b4', 'Female': '#e377c2'})
axes[0, 1].set_title('Pace vs. Physicality (Sampled)')
axes[0, 1].set_xlabel('Physic Rating')
axes[0, 1].set_ylabel('Pace Rating')

# Plot C: Boxplot for Physical Attributes (Height)
sns.boxplot(data=df_combined, x='Gender', y='height_cm', ax=axes[1, 0], palette={'Male': '#1f77b4', 'Female': '#e377c2'})
axes[1, 0].set_title('Height Distribution (cm)')
axes[1, 0].set_ylabel('Height (cm)')

# Plot D: Radar-style bar comparison for main football attributes
attrs = ['pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']
gender_means = df_combined.groupby('Gender')[attrs].mean().reset_index()
gender_melted = pd.melt(gender_means, id_vars=['Gender'], value_vars=attrs, var_name='Attribute', value_name='Average Rating')

sns.barplot(data=gender_melted, x='Attribute', y='Average Rating', hue='Gender', ax=axes[1, 1], palette={'Male': '#1f77b4', 'Female': '#e377c2'})
axes[1, 1].set_title('Average Core Football Attributes')
axes[1, 1].set_ylim(40, 75)

plt.tight_layout()
plt.savefig('gender_parity_eda.png', dpi=300)
plt.show()

print("--- Summary Statistics by Gender ---")
print(summary_stats.to_string())