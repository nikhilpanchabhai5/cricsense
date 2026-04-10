"""Build your first ML model - Predict match winner"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib
import os
import warnings

warnings.filterwarnings('ignore')

print("\n" + "=" * 60)
print("🤖 CricSense - First ML Model")
print("=" * 60 + "\n")

# Step 1: Load data
print("Step 1: Loading data...")
try:
    df = pd.read_csv('data/raw/ipl_matches.csv')
    print(f"✅ Loaded {len(df)} matches\n")
except FileNotFoundError:
    print("❌ CSV file not found. Run: python generate_sample_data.py")
    exit()

# Step 2: Create features
print("Step 2: Creating features...")

# Simple features for prediction
df['team1_is_toss_winner'] = (df['team1'] == df['toss_winner']).astype(int)
df['team1_bats_first'] = ((df['toss_decision'] == 'bat') & 
                          (df['toss_winner'] == df['team1'])).astype(int)

# Target: did team1 win?
df['team1_won'] = (df['winner'] == df['team1']).astype(int)

print("✅ Features created:\n")
print(df[['team1', 'team2', 'team1_is_toss_winner', 'team1_bats_first', 'team1_won']].head())

# Step 3: Prepare data
print("\n\nStep 3: Preparing data for ML...")

# Features (input)
feature_cols = ['team1_is_toss_winner', 'team1_bats_first']
X = df[feature_cols].fillna(0)

# Target (output)
y = df['team1_won']

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Step 4: Split data
print("\nStep 4: Splitting data (80% train, 20% test)...")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training set: {len(X_train)} samples")
print(f"Test set: {len(X_test)} samples")

# Step 5: Train model
print("\nStep 5: Training Random Forest model...")

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

print("✅ Model trained!")

# Step 6: Evaluate
print("\nStep 6: Evaluating model...")

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy:.2%}")
print(f"\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, 
    target_names=['Team 2 Wins', 'Team 1 Wins']))

# Step 7: Create scaler and save model
print("\nStep 7: Scaling features and preparing for save...")

scaler = StandardScaler()
scaler.fit(X_train)

print("✅ Scaler fitted!")

# Step 8: Create models directory
print("\nStep 8: Creating models directory...")

models_dir = 'data/models'
try:
    os.makedirs(models_dir, exist_ok=True)
    print(f"✅ Directory created/exists: {models_dir}")
except Exception as e:
    print(f"❌ Error creating directory: {e}")
    exit()

# Step 9: Save model
print("\nStep 9: Saving model and scaler...")

try:
    model_path = os.path.join(models_dir, 'match_predictor.pkl')
    scaler_path = os.path.join(models_dir, 'scaler.pkl')
    
    joblib.dump(model, model_path)
    print(f"✅ Model saved to: {model_path}")
    
    joblib.dump(scaler, scaler_path)
    print(f"✅ Scaler saved to: {scaler_path}")
    
    # Verify files exist
    if os.path.exists(model_path):
        print(f"✅ VERIFIED: {model_path} exists")
    else:
        print(f"❌ ERROR: {model_path} not created!")
    
    if os.path.exists(scaler_path):
        print(f"✅ VERIFIED: {scaler_path} exists")
    else:
        print(f"❌ ERROR: {scaler_path} not created!")
        
except Exception as e:
    print(f"❌ Error saving files: {e}")
    import traceback
    traceback.print_exc()
    exit()

# Step 10: Make a prediction
print("\nStep 10: Making a prediction...")

# Example: Team 1 won toss and is batting
example = pd.DataFrame({
    'team1_is_toss_winner': [1],
    'team1_bats_first': [1]
})

example_scaled = scaler.transform(example)
prediction = model.predict(example_scaled)[0]
probability = model.predict_proba(example_scaled)[0]

print(f"\nExample prediction:")
print(f"Team 1 won toss: YES")
print(f"Team 1 bats first: YES")
print(f"\nPrediction: {'Team 1 WINS' if prediction == 1 else 'Team 2 WINS'}")
print(f"Confidence: {probability[prediction]:.2%}")

print("\n" + "=" * 60)
print("🎉 Your first ML model is working!")
print("=" * 60)
print("\n✅ Model files created and saved!")
print("\nNext steps:")
print("1. Restart Flask API")
print("2. Test predictions via API")
print("3. Connect frontend to backend")
print("4. Add more features to improve accuracy\n")