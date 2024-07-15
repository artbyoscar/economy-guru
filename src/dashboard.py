# src/dashboard.py

import plotly.graph_objects as go

def create_savings_chart(dates, balances):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=balances, mode='lines+markers', name='Savings'))
    fig.update_layout(title='Savings Over Time', xaxis_title='Date', yaxis_title='Balance')
    fig.show()
