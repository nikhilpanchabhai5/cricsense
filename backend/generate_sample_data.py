"""
Sample IPL Data Generator
Generates realistic IPL match data for testing and learning

Run this to create sample data:
    py backend/generate_sample_data.py
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# IPL Teams
TEAMS = ['CSK', 'MI', 'RCB', 'KKR', 'DC', 'RR', 'SRH', 'PBKS', 'GT', 'LSG']

# Cricket Venues
VENUES = [
    'Wankhede Stadium', 'Eden Gardens', 'M.A. Chidambaram Stadium',
    'Arun Jaitley Stadium', 'Narendra Modi Stadium', 'Punjab Cricket Association IS Bindra Stadium',
    'Rajiv Gandhi International Cricket Stadium', 'TNPL Cricket Ground',
    'Barsapara Cricket Stadium', 'Sheikh Zayed Stadium'
]

PLAYERS = {
    'CSK': ['Ruturaj Gaikwad', 'MS Dhoni', 'Ravindra Jadeja', 'Dwayne Bravo'],
    'MI': ['Rohit Sharma', 'Suryakumar Yadav', 'Jasprit Bumrah', 'Hardik Pandya'],
    'RCB': ['Virat Kohli', 'Glenn Maxwell', 'Mohammed Siraj', 'Josh Hazlewood'],
    'KKR': ['Shreyas Iyer', 'Nitish Rana', 'Pat Cummins', 'Varun Chakaravarthy'],
    'DC': ['Rishabh Pant', 'David Warner', 'Mitchell Marsh', 'Anrich Nortje'],
    'RR': ['Sanju Samson', 'Jos Buttler', 'Yuzvendra Chahal', 'Trent Boult'],
    'SRH': ['Aiden Markram', 'Harry Brook', 'Bhuvneshwar Kumar', 'T Natarajan'],
    'PBKS': ['Shikhar Dhawan', 'Liam Livingstone', 'Kagiso Rabada', 'Sam Curran'],
    'GT': ['Hardik Pandya', 'Rashid Khan', 'Mohammed Shami', 'Sai Sudharsan'],
    'LSG': ['KL Rahul', 'Nicholas Pooran', 'Ravi Bishnoi', 'Mohsin Khan']
}

def generate_sample_matches(num_matches=100):
    """Generate sample IPL match data"""
    
    print(f"📊 Generating {num_matches} sample IPL matches...\n")
    
    matches = []
    start_date = datetime(2023, 3, 31)
    
    for i in range(num_matches):
        # Random teams (ensure they're different)
        team1, team2 = random.sample(TEAMS, 2)
        
        # Toss details
        toss_winner = random.choice([team1, team2])
        toss_decision = random.choice(['bat', 'bowl'])
        
        # Runs scored
        team1_runs = random.randint(130, 220)
        team2_runs = random.randint(130, 220)
        
        # Winner
        winner = team1 if team1_runs > team2_runs else team2
        
        # Player of the match
        pom_team = random.choice([team1, team2])
        pom = random.choice(PLAYERS[pom_team])
        
        # Match date
        match_date = start_date + timedelta(days=i)
        
        match = {
            'match_id': i + 1,
            'date': match_date.strftime('%Y-%m-%d'),
            'team1': team1,
            'team2': team2,
            'venue': random.choice(VENUES),
            'toss_winner': toss_winner,
            'toss_decision': toss_decision,
            'team1_runs': team1_runs,
            'team2_runs': team2_runs,
            'winner': winner,
            'winner_runs': abs(team1_runs - team2_runs),
            'player_of_match': pom,
            'overs_played': round(random.uniform(15, 20), 1)
        }
        
        matches.append(match)
    
    return pd.DataFrame(matches)

def generate_player_stats(num_players=50):
    """Generate player statistics"""
    
    print(f"🏃 Generating {num_players} player statistics...\n")
    
    players = []
    
    for team in TEAMS:
        team_players = PLAYERS[team]
        for player in team_players:
            player_data = {
                'player_name': player,
                'team': team,
                'matches_played': random.randint(10, 20),
                'runs_scored': random.randint(200, 1000),
                'avg_score': round(random.uniform(20, 60), 2),
                'strike_rate': round(random.uniform(100, 180), 2),
                'wickets_taken': random.randint(0, 15),
                'bowling_avg': round(random.uniform(15, 40), 2),
                'economy': round(random.uniform(6, 10), 2)
            }
            players.append(player_data)
    
    return pd.DataFrame(players)

def save_sample_data(matches_df, players_df, output_dir='backend/data/raw'):
    """Save sample data to CSV files"""
    
    # Create directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Save matches
    matches_path = os.path.join(output_dir, 'ipl_matches.csv')
    matches_df.to_csv(matches_path, index=False)
    print(f"✅ Saved matches data: {matches_path}")
    print(f"   Rows: {len(matches_df)}, Columns: {len(matches_df.columns)}\n")
    
    # Save players
    players_path = os.path.join(output_dir, 'ipl_players.csv')
    players_df.to_csv(players_path, index=False)
    print(f"✅ Saved players data: {players_path}")
    print(f"   Rows: {len(players_df)}, Columns: {len(players_df.columns)}\n")

def display_sample_data(matches_df, players_df):
    """Display sample of generated data"""
    
    print("\n" + "=" * 70)
    print("📋 SAMPLE MATCHES DATA")
    print("=" * 70 + "\n")
    print(matches_df.head(10).to_string(index=False))
    
    print("\n" + "=" * 70)
    print("📋 SAMPLE PLAYERS DATA")
    print("=" * 70 + "\n")
    print(players_df.head(10).to_string(index=False))
    
    print("\n" + "=" * 70)
    print("📊 DATA SUMMARY")
    print("=" * 70)
    print(f"\nMatches:")
    print(f"  Total matches: {len(matches_df)}")
    print(f"  Date range: {matches_df['date'].min()} to {matches_df['date'].max()}")
    print(f"  Teams involved: {matches_df['team1'].nunique()}")
    print(f"  Average runs (Team1): {matches_df['team1_runs'].mean():.2f}")
    print(f"  Average runs (Team2): {matches_df['team2_runs'].mean():.2f}")
    
    print(f"\nPlayers:")
    print(f"  Total players: {len(players_df)}")
    print(f"  Teams: {players_df['team'].nunique()}")
    print(f"  Avg runs per player: {players_df['runs_scored'].mean():.2f}")
    print(f"  Avg strike rate: {players_df['strike_rate'].mean():.2f}")
    
    print("\nColumn Names (Matches):")
    for i, col in enumerate(matches_df.columns, 1):
        print(f"  {i:2d}. {col}")
    
    print("\nColumn Names (Players):")
    for i, col in enumerate(players_df.columns, 1):
        print(f"  {i:2d}. {col}")

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🏏 CricSense Sample Data Generator")
    print("=" * 70 + "\n")
    
    # Generate data
    matches_df = generate_sample_matches(num_matches=100)
    players_df = generate_player_stats()
    
    # Display sample
    display_sample_data(matches_df, players_df)
    
    # Save to CSV
    print("\n" + "=" * 70)
    print("💾 SAVING DATA")
    print("=" * 70 + "\n")
    save_sample_data(matches_df, players_df)
    
    print("=" * 70)
    print("✅ SAMPLE DATA GENERATION COMPLETE!")
    print("=" * 70)
    print("""
You can now:

1. Explore the data:
   py backend/src/data_loader.py

2. Build a model:
   py backend/src/model_trainer.py

3. Make predictions:
   py backend/src/predictor.py

4. Start the API:
   py backend/app.py

Files created:
  - backend/data/raw/ipl_matches.csv
  - backend/data/raw/ipl_players.csv

Happy coding! 🚀
""")