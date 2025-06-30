**Stock Price Predictor**
A simple Project that is Flask web app that predicts future stock prices based on past data using linear regression.

**Features**
- Input number of days ahead.
- Get instant predicted price.
  
**Setup**
1. Install dependencies:
    pip install -r requirements.txt
2. Run the app:
    python app.py
   
**Note**
- Do not enter negative days.
- Make sure 'stock_prices.csv' is in the same folder.
- 'stock_prices.csv' should contain data about the stock with two columns:'Date' (e.g., '2023-01-01') and 'Close' prices (e.g., '100').
