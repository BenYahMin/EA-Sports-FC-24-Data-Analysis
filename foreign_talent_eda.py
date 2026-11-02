# Let's see if we can map leagues to countries or if we can use a heuristic (e.g., Premier League -> England, La Liga -> Spain)
# Let's create a dictionary mapping major leagues to their home countries
league_to_country = {
    'Premier League': 'England',
    'EFL Championship': 'England',
    'La Liga': 'Spain',
    'Serie A': 'Italy',
    'Bundesliga': 'Germany',
    'Ligue 1': 'France',
    'Eredivisie': 'Netherlands',
    'Liga Portugal': 'Portugal',
    'Super Lig': 'Turkey',
    'MLS': 'United States',
    'Saudi Pro League': 'Saudi Arabia',
    'Argentina Liga Profesional': 'Argentina',
    'Liga MX': 'Mexico',
    'Brasileirão Série A': 'Brazil'
}

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath = r"C:\Users\benja\Documents\Main\EA Sports FC 24\Datasets\male_players.csv"
df_male = pd.read_csv(filepath, low_memory = False)
df_foreign = df_male[df_male['league_name'].isin(league_to_country.keys())].copy()
df_foreign['home_country'] = df_foreign['league_name'].map(league_to_country)
df_foreign['is_foreign'] = df_foreign['nationality_name'] != df_foreign['home_country']

# Aggregate by league
foreign_stats = df_foreign.groupby('league_name').agg(
    total_players=('is_foreign', 'count'),
    foreign_players=('is_foreign', 'sum')
).reset_index()

foreign_stats['foreign_pct'] = (foreign_stats['foreign_players'] / foreign_stats['total_players']) * 100
foreign_stats = foreign_stats.sort_values(by='foreign_pct', ascending=False)

print("--- Foreign Player Percentage in Major Leagues ---")
print(foreign_stats.to_string(index=False))

# Visualization
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")
sns.barplot(data=foreign_stats, y='league_name', x='foreign_pct', palette='crest')
plt.title('Percentage of Foreign (Non-Domestic) Players by League', fontsize=14, fontweight='bold')
plt.xlabel('Foreign Players (%)', fontsize=12)
plt.ylabel('League Name', fontsize=12)

for i, v in enumerate(foreign_stats['foreign_pct']):
    plt.text(v + 1, i, f"{v:.1f}%", va='center', fontsize=10)

plt.tight_layout()
plt.savefig('foreign_players_eda.png', dpi=300)
plt.show()