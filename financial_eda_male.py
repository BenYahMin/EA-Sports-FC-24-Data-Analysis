import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# I loaded the males dataset
filepath = r"C:\Users\benja\Documents\Main\EA Sports FC 24\Datasets\male_players.csv"
df_male = pd.read_csv(filepath, low_memory=False)

# will use this for wage analysis
cols = ['short_name', 'age', 'overall', 'potential', 'value_eur', 'wage_eur']
df_fin = df_male[cols].dropna(subset=['value_eur', 'wage_eur']).copy()

# Basic Descriptive Statistics
stats = df_fin[['overall', 'age', 'value_eur', 'wage_eur']].describe()

# Correlation Matrix
correlation = df_fin[['overall', 'age', 'potential', 'value_eur', 'wage_eur']].corr()

# The Age Premium (Average Value and Wage by Age)
# i Filterd for realistic ages for a clean chart
df_age = df_fin[(df_fin['age'] >= 16) & (df_fin['age'] <= 40)]
age_grouped = df_age.groupby('age')[['value_eur', 'wage_eur']].mean().reset_index()

# Set up the visualization style before doing the visualizations
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot A: Overall Rating vs. Wages (Scatterplot)
sns.scatterplot(data=df_fin, x='overall', y='wage_eur', alpha=0.3, color='blue', ax=axes[0])
axes[0].set_title('Overall Rating vs. Weekly Wage (€)', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Overall Rating')
axes[0].set_ylabel('Wage (€)')
# Format y-axis to show millions/thousands
axes[0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# Plot B: The Age Premium (Line plot of Value by Age)
sns.lineplot(data=age_grouped, x='age', y='value_eur', marker='o', color='green', ax=axes[1], linewidth=2.5)
axes[1].set_title('Average Market Value by Age (The Age Premium)', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Age')
axes[1].set_ylabel('Average Market Value (€)')
axes[1].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

plt.tight_layout()
plt.savefig('financial_eda.png', dpi=300)
plt.show()

print("--- Descriptive Statistics ---")
print(stats.to_string())
print("\n--- Correlation Matrix ---")
print(correlation.to_string())
print("\n--- Peak Market Value Age ---")
peak_age = age_grouped.loc[age_grouped['value_eur'].idxmax()]
print(f"Age with highest average value: {peak_age['age']} years old (€{peak_age['value_eur']:,.0f})")