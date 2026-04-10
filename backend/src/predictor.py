"""
Match Predictor - Load trained model and make predictions
"""

import os
import joblib
import pandas as pd

class MatchPredictor:
    def __init__(self):
        model_path = 'data/models/match_predictor.pkl'
        scaler_path = 'data/models/scaler.pkl'
        
        # Check if models exist
        if os.path.exists(model_path) and os.path.exists(scaler_path):
            self.model = joblib.load(model_path)
            self.scaler = joblib.load(scaler_path)
            print("✅ Trained models loaded successfully")
            self.is_ready = True
        else:
            print("⚠️  Trained models not found yet. Please train a model first.")
            self.model = None
            self.scaler = None
            self.is_ready = False
    
    def predict(self, features_dict):
        """Make a prediction from features"""
        
        if not self.is_ready:
            return {'error': 'Model not trained yet. Run build_first_model.py first.'}
        
        try:
            features_df = pd.DataFrame([features_dict])
            features_scaled = self.scaler.transform(features_df)
            
            prediction = self.model.predict(features_scaled)[0]
            probability = self.model.predict_proba(features_scaled)[0]
            
            return {
                'prediction': int(prediction),
                'probability': float(probability[1])
            }
        except Exception as e:
            return {'error': str(e)}


# Test code (runs when file is imported at module level)
if __name__ == "__main__":
    # This runs only if you run this file directly
    # Not when imported by app.py
    predictor = MatchPredictor()
    
    if predictor.is_ready:
        # Test with sample features
        test_features = {
            'team1_is_toss_winner': 1,
            'team1_bats_first': 1
        }
        result = predictor.predict(test_features)
        print(f"\n✅ Test prediction: {result}")
    else:
        print("\n❌ Models not available. Train first with: python src/build_first_model.py")