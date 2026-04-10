# feature_engineering.py
import pandas as pd

def create_features(df):
    """Create ML features from raw data"""
    
    # 1. Team performance features
    df['team1_avg_runs'] = df.groupby('team1')['team1_runs'].transform('mean')
    df['team2_avg_runs'] = df.groupby('team2')['team2_runs'].transform('mean')
    
    # 2. Venue advantage
    df['team1_venue_avg'] = df.groupby(['team1', 'venue'])['team1_runs'].transform('mean')
    
    # 3. Recent form (last 5 matches)
    df['team1_recent_wins'] = df.groupby('team1')['winner'].apply(
        lambda x: (x == x.index[0]).rolling(5).sum()
    )
    
    # 4. Toss advantage
    df['toss_winner_bat'] = (df['toss_winner'] == df['team1']).astype(int) & \
                            (df['toss_decision'] == 'bat').astype(int)
    
    # 5. Target feature (what we want to predict)
    df['team1_win'] = (df['winner'] == df['team1']).astype(int)
    
    return df

# Usage
matches_df = pd.read_csv('data/raw/ipl_matches.csv')
matches_df = create_features(matches_df)
matches_df.to_csv('data/processed/matches_with_features.csv', index=False)