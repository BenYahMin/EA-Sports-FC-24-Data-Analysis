import pandas as pd

# Load the dataset
filepath = r"C:\Users\benja\Documents\Main\EA Sports FC 24\Datasets\male_players.csv"
df_male = pd.read_csv(filepath, low_memory=False)

# Select relevant columns
cols = ['short_name', 'long_name', 'age', 'overall', 'potential', 'value_eur', 'wage_eur', 
        'club_name', 'league_name', 'player_positions', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']
df = df_male[cols].dropna(subset=['value_eur', 'wage_eur']).copy()


# Define the criteria for a "Hidden Gem"
# 1. Young (Age <= 21)
# 2. High Potential (Potential >= 83)
# 3. Affordable Market Value (Value <= €5,000,000)
# 4. Low Wages (Wage <= €10,000/week)

hidden_gems_male = df[
    (df['age'] <= 21) & 
    (df['potential'] >= 83) & 
    (df['value_eur'] <= 5000000) & 
    (df['wage_eur'] <= 10000)
].sort_values(by='potential', ascending=False)

# Save to a new CSV file
output_filename = "male_hidden_gems_complete_list.csv"
hidden_gems_male.to_csv(output_filename, index=False)

print(f"Successfully generated '{output_filename}' containing {len(hidden_gems_male)} players.")
print(hidden_gems_male[['short_name', 'age', 'overall', 'potential', 'value_eur', 'wage_eur', 'club_name']].head(10).to_string(index=False))