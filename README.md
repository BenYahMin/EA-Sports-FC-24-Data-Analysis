# Data Analytics Portfolio Project: EA Sports FC 24 Comprehensive Analysis

## 1. Introduction & Project Overview
This project presents a comprehensive, end-to-end data analytics investigation into the EA Sports FC 24 player and team datasets (`male_players.csv`, `female_players.csv`, `male_teams.csv`, `female_teams.csv`, etc.). Adopting the role of a professional sports data analyst, this study moves from raw data cleaning and exploratory data analysis (EDA) to actionable business insights and recommendations.

## 2. Methodology & Analytical Pillars
The analysis is divided into six core analytical pillars:
1. **Financial & Valuation Analysis:** Investigating the exponential relationship between overall player ratings and weekly wages, alongside mapping the player "market value age curve".
2. **Scouting & Valuation Arbitrage ("Hidden Gems"):** Building strict filtering algorithms to identify young, high-potential, and affordable talent across both male and female player pools.
3. **Physical & Technical Attributes:** Comparing positional specializations (Center Backs vs. Strikers) across the six core FIFA attributes.
4. **Gender Parity & Population Distributions:** Examining rating calibration differences, demographic divergences, and structural distributions between male and female datasets.
5. **League Financial Disparities:** Quantifying wage bill stratification and average pay across global football leagues.
6. **Domestic vs. Foreign Talent Ratios:** Analyzing globalization and the percentage of imported players across major leagues.

---

## 3. Key Findings & Business Insights

### Pillar 1: Financial Valuation & The Age Peak
* **Wage Scalability:** Player wages scale exponentially rather than linearly. While average players (66 overall) earn roughly €4,000/week, elite players (85+) command salaries exceeding hundreds of thousands of euros.
* **The Market Value Curve:** Player valuations form a distinct bell curve. Male player market values peak precisely at **age 26** (€3.27M average), while female player market values peak at **age 28** (€20M average) before experiencing steep depreciation.

### Pillar 2: Hidden Gems (Scouting Arbitrage)
* **Male Dataset:** Filtering for players aged $\le 21$, potential $\ge 83$, value $\le €5	ext{M}$, and wages $\le €10,000$ yields 821 high-value acquisition targets (e.g., Jude Bellingham, A. Gomes, J. Doku).
* **Female Dataset:** Adjusting parameters for compressed wage tiers ($\le €600/	ext{week}$) isolates 48 elite youth prospects (e.g., M. Symonds, Ona Baradad, Ari Mingueza).

### Pillar 3: Positional Specialization (CB vs. ST)
* **Polarized Profiles:** Strikers heavily dominate in Pace, Shooting, and Dribbling, while Center Backs lead in Defending and Physic.
* **Modern Tactical Shift:** The narrow gap in Passing attributes (52.6 for ST vs. 47.8 for CB in males; 62.0 vs. 56.5 in females) highlights that modern center-backs require advanced ball-playing competence.

### Pillar 4: Gender Parity & Dataset Calibration
* **Rating Calibration:** The female dataset averages a 75.0 overall rating compared to the male dataset's 65.9. This reflects a **selection bias / tier difference**: the male dataset includes over 180,000 players down to global lower tiers, whereas the female dataset (~5,000 players) represents the elite tier of professional women's football.
* **Modeling Warning:** Male and female datasets represent independent statistical populations and must never be combined into a single predictive pricing model.

### Pillar 5: League Financial Disparities
* **Premier League Hegemony:** The English Premier League operates in a financial stratosphere, averaging **€36,535/week** per player with a total weekly wage bill exceeding **€341 million**.
* **Global Stratification:** Top Premier League players earn over 70 times more than professionals in lower-tier European leagues (e.g., Veikkausliiga ~€511/week).

### Pillar 6: Domestic vs. Foreign Talent
* **Global Hubs:** The Premier League and Serie A are the most internationalized leagues globally, with **over 72%** foreign players.
* **Domestic Reliance:** La Liga and Liga MX rely far more heavily on domestic pipelines, maintaining foreign player ratios below 36%.

---

## 4. Strategic Recommendations
1. **Acquisition Timing:** Clubs should target player acquisitions between ages 19–21 and divest or re-negotiate before age 26 (males) or 28 (females) to maximize resale value.
2. **Recruitment Arbitrage:** Utilize multi-factor scouting filters (Potential vs. Current Value) rather than relying on current overall ratings, capturing high-ROI youth talent before wage inflation occurs.
3. **Independent Modeling:** Separate machine learning models must be maintained for male and female player evaluations due to differing wage structures and rating calibrations.
