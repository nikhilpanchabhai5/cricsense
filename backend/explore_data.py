"""Explore IPL data"""

import pandas as pd
import numpy as np

# Load matches
df_matches = pd.read_csv('backend/data/raw/ipl_matches.csv')

print("📊 MATCHES DATA")
print(f"Shape: {df_matches.shape}")
print(f"\nFirst few rows:")
print(df_matches.head())

print(f"\nData types:")
print(df_matches.dtypes)

print(f"\nBasic statistics:")
print(df_matches.describe())

print(f"\nWinning teams distribution:")
print(df_matches['winner'].value_counts())

# Load players
df_players = pd.read_csv('backend/data/raw/ipl_players.csv')

print("\n\n🏃 PLAYERS DATA")
print(f"Shape: {df_players.shape}")
print(f"\nTop batsmen by runs:")
print(df_players.nlargest(5, 'runs_scored')[['player_name', 'team', 'runs_scored', 'strike_rate']])

print(f"\nTop bowlers by wickets:")
print(df_players.nlargest(5, 'wickets_taken')[['player_name', 'team', 'wickets_taken', 'economy']])