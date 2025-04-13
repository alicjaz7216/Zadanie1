#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['POST'])
def predict():
    data = request.get_json()

    number1 = data.get('number1', 0)
    number2 = data.get('number2', 0)

    try:
        num1 = float(number1)
    except (TypeError, ValueError):
        num1 = 0

    try:
        num2 = float(number2)
    except (TypeError, ValueError):
        num2 = 0

    total = num1 + num2
    prediction = 1 if total > 5.8 else 0

    response = {
        "features": {
            "number1": num1,
            "number2": num2
        },
        "prediction": prediction
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

