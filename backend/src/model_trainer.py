# model_trainer.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

def train_match_prediction_model():
    """Train model to predict match winner"""
    
    # 1. Load processed data
    df = pd.read_csv('data/processed/matches_with_features.csv')
    
    # 2. Select features (input)
    feature_columns = [
        'team1_avg_runs', 'team2_avg_runs', 
        'team1_venue_avg', 'team1_recent_wins',
        'toss_winner_bat'
    ]
    X = df[feature_columns].fillna(0)  # Handle missing values
    
    # 3. Select target (what to predict)
    y = df['team1_win']
    
    # 4. Split data: 80% train, 20% test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"Training set size: {len(X_train)}")
    print(f"Test set size: {len(X_test)}")
    
    # 5. Scale features (normalize)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 6. Train model
    model = RandomForestClassifier(
        n_estimators=100,      # 100 trees
        max_depth=10,          # Tree depth limit
        random_state=42,
        n_jobs=-1              # Use all CPU cores
    )
    
    print("Training model...")
    model.fit(X_train_scaled, y_train)
    print("Training complete!")
    
    # 7. Evaluate
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n{'='*50}")
    print(f"Model Accuracy: {accuracy:.2%}")
    print(f"{'='*50}")
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    print("\nDetailed Report:")
    print(classification_report(y_test, y_pred, 
        target_names=['Team 2 Wins', 'Team 1 Wins']))
    
    # 8. Save model
    joblib.dump(model, 'data/models/match_predictor.pkl')
    joblib.dump(scaler, 'data/models/scaler.pkl')
    
    # 9. Feature importance
    importance_df = pd.DataFrame({
        'feature': feature_columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\nFeature Importance:")
    print(importance_df)
    
    return model, scaler

if __name__ == "__main__":
    train_match_prediction_model()