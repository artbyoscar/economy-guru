from flask import Flask, request, jsonify
from debt_calculator import calculate_debt_free_months

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    debts = data['debts']
    budget = data['budget']
    months = calculate_debt_free_months(debts, budget)
    return jsonify({"months_to_debt_free": months})

if __name__ == '__main__':
    app.run(debug=True)
