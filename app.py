from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
import traceback
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load the trained model
try:
    with open('goldmansachs_price_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Features used in the model - UPDATED based on your training code
FEATURES = ['Returns', 'MA_7', 'MA_30', 'Volatility', 'Volume_Change',
            'Close_lag_1', 'Close_lag_2', 'Close_lag_3', 'Close_lag_4',
            'Close_lag_5', 'Close_lag_7', 'Day', 'Month', 'Week']

def prepare_input_data(input_data):
    """Prepare input data for prediction"""
    try:
        # Create a DataFrame with all required features
        df = pd.DataFrame([input_data])
        
        # Ensure all required columns are present
        for feature in FEATURES:
            if feature not in df.columns:
                df[feature] = 0
        
        # Reorder columns to match training
        df = df[FEATURES]
        
        return df
    except Exception as e:
        print(f"Error preparing data: {e}")
        return None

@app.route('/')
def home():
    """Home page with input form"""
    current_date = datetime.now().strftime('%Y-%m-%d')
    return render_template('index.html', current_date=current_date)

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests"""
    if model is None:
        return jsonify({'error': 'Model not loaded properly'}), 500
    
    try:
        # Extract form data
        data = request.form.to_dict()
        
        # Convert string inputs to float
        input_data = {}
        for key, value in data.items():
            try:
                input_data[key] = float(value)
            except:
                input_data[key] = 0.0
        
        # Prepare the data
        prepared_data = prepare_input_data(input_data)
        
        if prepared_data is None:
            return jsonify({'error': 'Error preparing input data'}), 400
        
        # Make prediction
        prediction = model.predict(prepared_data)[0]
        
        # Get current date for display - FIXED SYNTAX ERROR HERE
        current_date = datetime.now().strftime('%B %d, %Y')
        
        # Render result template with prediction
        return render_template('result.html',
                             prediction=f"{prediction:.2f}",
                             current_date=current_date,
                             input_data=input_data)
    
    except Exception as e:
        print(f"Prediction error: {e}")
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for prediction"""
    if model is None:
        return jsonify({'error': 'Model not loaded properly'}), 500
    
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        # Prepare the data
        prepared_data = prepare_input_data(data)
        
        if prepared_data is None:
            return jsonify({'error': 'Error preparing input data'}), 400
        
        # Make prediction
        prediction = model.predict(prepared_data)[0]
        
        return jsonify({
            'predicted_price': float(prediction),
            'currency': 'USD',
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)