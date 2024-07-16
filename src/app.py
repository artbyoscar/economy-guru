from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Ensure the model path is correct
model_path = '/workspace/economy-guru/logistic_model.pkl'  # Adjust the path if necessary

# Load the model
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [data['V1'], data['V2'], data['V3'], data['V4'], data['V5'], data['V6'], data['V7'], data['V8'], data['V9'], data['V10'],
                data['V11'], data['V12'], data['V13'], data['V14'], data['V15'], data['V16'], data['V17'], data['V18'], data['V19'], data['V20'],
                data['V21'], data['V22'], data['V23'], data['V24'], data['V25'], data['V26'], data['V27'], data['V28'], data['Amount']]
    
    prediction = model.predict([features])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
