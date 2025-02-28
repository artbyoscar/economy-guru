from flask import Flask, request, jsonify
import joblib
import pandas as pd
import logging

# Initialize the Flask app
app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ensure the model path is correct
model_path = '/workspace/economy-guru/logistic_model.pkl'  # Adjust the path if necessary

# Load the model
try:
    model = joblib.load(model_path)
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model: {e}")

@app.route('/')
def home():
    return "Welcome to the Economy Guru Prediction API! Use the /predict endpoint to get predictions."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    required_features = [
        'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 
        'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 
        'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 
        'Amount'
    ]
    
    try:
        # Check if all required features are present
        features = {feature: [data[feature]] for feature in required_features}
    except KeyError as e:
        logger.error(f"Missing feature: {e}")
        return jsonify({'error': f'Missing feature: {str(e)}'}), 400

    df_features = pd.DataFrame(features)
    try:
        prediction = model.predict(df_features)
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return jsonify({'error': f'Error during prediction: {str(e)}'}), 500
    
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
