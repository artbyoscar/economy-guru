# src/financial_data.py

import plaid
from plaid.api import plaid_api

def get_transactions(access_token):
    client = plaid.Client(client_id='YOUR_CLIENT_ID', secret='YOUR_SECRET', environment='sandbox')
    response = client.Transactions.get(access_token, start_date='2023-01-01', end_date='2023-12-31')
    return response['transactions']
