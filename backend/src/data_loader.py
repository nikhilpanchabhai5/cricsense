# data_loader.py
import pandas as pd
import numpy as np

def load_ipl_data():
    """Load IPL match data from CSV"""
    df = pd.read_csv('data/raw/ipl_matches.csv')
    
    print(f"Dataset shape: {df.shape}")  # (rows, columns)
    print(f"\nFirst 5 rows:")
    print(df.head())
    
    print(f"\nColumn info:")
    print(df.info())
    
    print(f"\nMissing values:")
    print(df.isnull().sum())
    
    print(f"\nBasic statistics:")
    print(df.describe())
    
    return df

if __name__ == "__main__":
    matches_df = load_ipl_data()