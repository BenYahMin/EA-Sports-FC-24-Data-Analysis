import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath = r"C:\Users\benja\Documents\Main\EA Sports FC 24\Datasets\male_players.csv"
df_male = pd.read_csv(filepath, low_memory=False)

# Select relevant columns for league financial analysis
cols = ['league_name', 'value_eur', 'wage_eur']
df_leagues = df_male[cols].dropna().copy()

# Group by league and calculate financial metrics
league_stats = df_leagues.groupby('league_name').agg(
    total_players=('wage_eur', 'count'),
    mean_wage=('wage_eur', 'mean'),
    total_wage_bill=('wage_eur', 'sum'),
    mean_value=('value_eur', 'mean'),
    total_value=('value_eur', 'sum')
).reset_index()

# Filter out leagues with too few players (e.g., less than 100) to ensure statistical significance
league_stats = league_stats[league_stats['total_players'] >= 100]

# Sort by Mean Wage to find the richest leagues on average
top_mean_wage = league_stats.sort_values(by='mean_wage', ascending=False).head(10)

# Sort by Total Wage Bill to find the leagues with the highest overall spending
top_total_wage = league_stats.sort_values(by='total_wage_bill', ascending=False).head(10)

# Visualization
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(18, 7))
fig.suptitle('Financial Disparities Between Leagues (Male Dataset)', fontsize=16, fontweight='bold')

# Plot A: Top 10 Leagues by Average Weekly Wage
sns.barplot(data=top_mean_wage, y='league_name', x='mean_wage', ax=axes[0], palette='viridis')
axes[0].set_title('Top 10 Leagues by Average Weekly Wage (€)')
axes[0].set_xlabel('Average Weekly Wage (€)')
axes[0].set_ylabel('')
axes[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# Add data labels
for i, v in enumerate(top_mean_wage['mean_wage']):
    axes[0].text(v + 1000, i, f"€{v:,.0f}", va='center', fontsize=10)

# Plot B: Top 10 Leagues by Total Weekly Wage Bill
sns.barplot(data=top_total_wage, y='league_name', x='total_wage_bill', ax=axes[1], palette='magma')
axes[1].set_title('Top 10 Leagues by Total Weekly Wage Bill (€)')
axes[1].set_xlabel('Total Weekly Wage Bill (€)')
axes[1].set_ylabel('')
axes[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# Add data labels
for i, v in enumerate(top_total_wage['total_wage_bill']):
    axes[1].text(v + 100000, i, f"€{v:,.0f}", va='center', fontsize=10)

plt.tight_layout()
plt.savefig('league_finances_eda.png', dpi=300)
plt.show()

# Print stats for context
print("--- Top 5 Leagues by Mean Wage ---")
print(top_mean_wage[['league_name', 'mean_wage', 'mean_value']].head(5).to_string(index=False))
print("\n--- Bottom 5 Leagues by Mean Wage (Out of valid leagues) ---")
bottom_mean_wage = league_stats.sort_values(by='mean_wage', ascending=True).head(5)
print(bottom_mean_wage[['league_name', 'mean_wage', 'mean_value']].to_string(index=False))