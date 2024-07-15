# src/ml_models.py

from sklearn.linear_model import LinearRegression
import numpy as np

def predict_savings_growth(current_savings, monthly_contribution, num_months):
    X = np.array(range(num_months)).reshape(-1, 1)
    y = current_savings + monthly_contribution * X
    model = LinearRegression().fit(X, y)
    return model.predict(X)
