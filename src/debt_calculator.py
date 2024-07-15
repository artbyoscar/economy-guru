import numpy as np

def calculate_debt_free_months(debts, budget):
    months = 0
    while any(debt['balance'] > 0 for debt in debts):
        debts.sort(key=lambda x: x['rate'], reverse=True)
        remaining_budget = budget
        for debt in debts:
            if debt['balance'] > 0:
                payment = min(debt['min_payment'], debt['balance'])
                if remaining_budget >= payment:
                    debt['balance'] -= payment
                    remaining_budget -= payment
                else:
                    debt['balance'] -= remaining_budget
                    remaining_budget = 0
        months += 1
    return months
