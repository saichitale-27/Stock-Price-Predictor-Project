from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os

app = Flask(__name__)

data = pd.read_csv('stock_prices.csv')
data['Date'] = pd.to_datetime(data['Date'])
data['Days'] = (data['Date'] - data['Date'].min()).dt.days
X = data[['Days']]
y = data['Close']

model = LinearRegression()
model.fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        days_ahead = int(request.form['days'])
        if days_ahead < 0:
            prediction = 'Days cannot be negative. Please enter a positive number.'
        else:
            future_day = np.array([[data['Days'].max() + days_ahead]])
            prediction = model.predict(future_day)[0]
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
