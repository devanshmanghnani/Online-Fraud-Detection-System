from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    amount = float(request.form['amount'])
    oldbalanceOrg = float(request.form['oldbalanceOrg'])
    newbalanceOrig = float(request.form['newbalanceOrig'])
    oldbalanceDest = float(request.form['oldbalanceDest'])
    newbalanceDest = float(request.form['newbalanceDest'])
    tx_type = request.form['type']

    # Assume default step (or let user select later)
    step = 1.0

    # One-hot encode the transaction type
    type_CASH_IN = 1 if tx_type == 'CASH_IN' else 0
    type_CASH_OUT = 1 if tx_type == 'CASH_OUT' else 0
    type_DEBIT = 1 if tx_type == 'DEBIT' else 0
    type_PAYMENT = 1 if tx_type == 'PAYMENT' else 0
    type_TRANSFER = 1 if tx_type == 'TRANSFER' else 0

    # Create feature array
    features = np.array([[step, amount, oldbalanceOrg, newbalanceOrig,
                          oldbalanceDest, newbalanceDest,
                          type_CASH_IN, type_CASH_OUT, type_DEBIT,
                          type_PAYMENT, type_TRANSFER]])

    # Scale the features
    features_scaled = scaler.transform(features)

    # Predict
    prediction = model.predict(features_scaled)

    if prediction[0] == 1:
        result = "Fraudulent Transaction Detected!"
    else:
        result = "Transaction is Safe."

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
