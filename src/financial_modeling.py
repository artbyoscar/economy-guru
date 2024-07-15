# src/financial_modeling.py

import numpy as np

def monte_carlo_simulation(initial_balance, num_simulations, num_years, mean_return, std_deviation):
    results = []
    for _ in range(num_simulations):
        balance = initial_balance
        for _ in range(num_years):
            balance += np.random.normal(mean_return, std_deviation)
        results.append(balance)
    return results
