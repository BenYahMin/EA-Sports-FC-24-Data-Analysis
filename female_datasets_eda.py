import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load female players dataset
female_filepath = r"C:\Users\benja\Documents\Main\EA Sports FC 24\Datasets\female_players.csv"
df_female = pd.read_csv(female_filepath, low_memory=False)

# Check for financial columns and non-null counts
cols_to_check = ['short_name', 'age', 'overall', 'potential', 'value_eur', 'wage_eur', 'player_positions']
print("Columns present:", [c for c in cols_to_check if c in df_female.columns])

if 'value_eur' in df_female.columns and 'wage_eur' in df_female.columns:
    print("Non-null value_eur:", df_female['value_eur'].notna().sum())
    print("Non-null wage_eur:", df_female['wage_eur'].notna().sum())

df_fin_f = df_female.dropna(subset=['value_eur', 'wage_eur'])
print(df_fin_f[['value_eur', 'wage_eur']].describe())




# Load the dataset
df_female = pd.read_csv(female_filepath, low_memory=False)


cols_fin = ['short_name', 'age', 'overall', 'potential', 'value_eur', 'wage_eur']
df_fin_f = df_female[cols_fin].dropna(subset=['value_eur', 'wage_eur']).copy()

# The Age Premium (Average Value by Age)
df_age_f = df_fin_f[(df_fin_f['age'] >= 16) & (df_fin_f['age'] <= 40)]
age_grouped_f = df_age_f.groupby('age')[['value_eur']].mean().reset_index()

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot A: Overall Rating vs. Wages
sns.scatterplot(data=df_fin_f, x='overall', y='wage_eur', alpha=0.5, color='magenta', ax=axes[0])
axes[0].set_title('Female Players: Overall Rating vs. Weekly Wage (€)', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Overall Rating')
axes[0].set_ylabel('Wage (€)')
axes[0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# Plot B: Average Market Value by Age
sns.lineplot(data=age_grouped_f, x='age', y='value_eur', marker='o', color='purple', ax=axes[1], linewidth=2.5)
axes[1].set_title('Female Players: Average Market Value by Age', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Age')
axes[1].set_ylabel('Average Market Value (€)')
axes[1].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

plt.tight_layout()
plt.savefig('female_financial_eda.png', dpi=300)
plt.show()

# 2. HIDDEN GEMS (FEMALE)
# Adjusting criteria for female dataset realities (lower wages, different value scaling)
hidden_gems_f = df_female[
    (df_female['age'] <= 21) & 
    (df_female['potential'] >= 83) & 
    (df_female['value_eur'] <= 5000000) & 
    (df_female['wage_eur'] <= 600)  # Median wage is 600
].sort_values(by='potential', ascending=False)

top_gems_f = hidden_gems_f[['short_name', 'age', 'overall', 'potential', 'value_eur', 'wage_eur', 'club_name']].head(10)
print("--- Top Female Hidden Gems ---")
print(top_gems_f.to_string(index=False))
print(f"\nTotal Female Hidden Gems found out of {len(df_fin_f)} players: {len(hidden_gems_f)}")


df_female['primary_position'] = df_female['player_positions'].astype(str).apply(lambda x: x.split(',')[0].strip())
df_pos_f = df_female[df_female['primary_position'].isin(['CB', 'ST'])].copy()

attributes = ['pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']
df_pos_f = df_pos_f.dropna(subset=attributes)
pos_means_f = df_pos_f.groupby('primary_position')[attributes].mean().reset_index()

pos_melted_f = pd.melt(pos_means_f, id_vars=['primary_position'], value_vars=attributes, 
                       var_name='Attribute', value_name='Average Rating')

plt.figure(figsize=(10, 6))
barplot_f = sns.barplot(
    data=pos_melted_f, 
    x='Attribute', 
    y='Average Rating', 
    hue='primary_position', 
    palette={'CB': '#1f77b4', 'ST': '#d62728'}
)

plt.title('Female Attribute Comparison: Center Backs (CB) vs. Strikers (ST)', fontsize=14, fontweight='bold')
plt.xlabel('Player Attribute', fontsize=12)
plt.ylabel('Average Rating', fontsize=12)
plt.legend(title='Position')
plt.ylim(20, 80)

for p in barplot_f.patches:
    barplot_f.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points')

plt.tight_layout()
plt.savefig('female_attributes_comparison.png', dpi=300)
plt.show()