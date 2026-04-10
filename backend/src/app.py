from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
import os

# Add src folder to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from predictor import MatchPredictor
import pandas as pd

app = Flask(__name__)
CORS(app)

predictor = MatchPredictor()

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'API is running!'})

@app.route('/api/teams', methods=['GET'])
def get_teams():
    teams = ['CSK', 'MI', 'RCB', 'KKR', 'DC', 'RR', 'SRH', 'PBKS', 'GT', 'LSG']
    return jsonify({'teams': teams})

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        if not all(k in data for k in ['team1', 'team2', 'venue', 'toss_winner', 'toss_decision']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Create features
        features = {
            'team1_is_toss_winner': 1 if data.get('toss_winner') == data.get('team1') else 0,
            'team1_bats_first': 1 if (data.get('toss_decision') == 'bat' and data.get('toss_winner') == data.get('team1')) else 0
        }
        
        # Use the correct method: predict (not predict_match)
        result = predictor.predict(features)
        
        if 'error' in result:
            return jsonify(result), 400
        
        return jsonify({
            'team1': data.get('team1'),
            'team2': data.get('team2'),
            'venue': data.get('venue'),
            'predicted_winner': data.get('team1') if result['prediction'] == 1 else data.get('team2'),
            'team1_win_probability': result['probability'],
            'team2_win_probability': 1 - result['probability']
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats/<team>', methods=['GET'])
def get_team_stats(team):
    try:
        df = pd.read_csv('data/raw/ipl_matches.csv')
        team_data = df[df['team1'] == team]
        
        if len(team_data) == 0:
            return jsonify({'error': f'Team {team} not found'}), 404
        
        stats = {
            'team': team,
            'matches_played': len(team_data),
            'wins': len(team_data[team_data['winner'] == team]),
            'avg_runs_scored': float(team_data['team1_runs'].mean()),
            'win_percentage': float((len(team_data[team_data['winner'] == team]) / len(team_data) * 100)) if len(team_data) > 0 else 0
        }
        
        return jsonify(stats)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("🏏 CricSense API")
    print("=" * 60)
    print("\n🚀 Starting Flask server...")
    print("📍 API running at: http://127.0.0.1:5000")
    print("\n📚 Available endpoints:")
    print("   GET  /api/health           - Check if API is running")
    print("   GET  /api/teams            - Get list of teams")
    print("   POST /api/predict          - Predict match winner")
    print("   GET  /api/stats/<team>     - Get team statistics")
    print("\n" + "=" * 60 + "\n")
    
    app.run(debug=True, port=5000)