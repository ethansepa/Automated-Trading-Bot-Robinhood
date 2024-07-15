from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score

import yfinance as yf # calls Yahoo Finance api to download daily stock and index prices
import pandas as pd

from backend.ml_model.utilities.order_types import OrderType

class BaseModel:
    def __init__(self, ticker="^GSPC", tolerance=0.05):
        # Create model
        self.model = RandomForestClassifier(n_estimators=200, min_samples_split=50, random_state=1)
        self.stock = yf.Ticker(ticker)
        self.stock_history = self.stock.history(period="max")
        self.tolerance = tolerance
        self.predictors = []
    
    def __clean_stock_historical_data(self):
        # Remove unneccesary collumns in the data
        del self.stock_history["Dividends"]
        del self.stock_history["Stock Splits"]

        # Create a Target to train ML Model by comparing if tommorows price is higher than todays model
        self.stock_history["Tomorrow"] = self.stock_history["Close"].shift(-1)
        self.stock_history["Target"] = (self.stock_history["Tomorrow"] > self.stock_history["Close"]).astype(int)

        # Remove old data
        self.stock_history = self.stock_history.loc["1995-01-01":].copy()
        self.__create_predictors__()
        self.stock_history.dropna()


    def __create_predictors__(self):
        # Create predictors
        self.predictors = []

    # Make prediction, only buy stock if at least 55% confident it will go up
    def __predict__(self, train, test):
        self.model.fit(train[self.predictors], train["Target"])
        preds = self.model.predict_proba(test[self.predictors])[:,1]
        preds[preds >= 0.6] = 1
        preds[preds < 0.6] = 0
        preds = pd.Series(preds, index=test.index, name="Predictions")
        return pd.concat([test["Target"], preds], axis=1)

    # Backtest starting with last 2 years of data and step by 100 days (≈250 trading days in a year)
    def __backtest__(self, start=500, step=100):
        all_predictions = []
        for i in range (start, self.stock_history.shape[0], step):
            train = self.stock_history.iloc[0:i].copy()
            test = self.stock_history.iloc[i:(i+step)].copy()
            predictions = self.__predict__(train, test)
            all_predictions.append(predictions)
        return pd.concat(all_predictions)
    
    def __next_prediction__(self):
        test = self.stock_history.iloc[-1:].copy()
        return self.model.predict_proba(test[self.predictors])[:,1]
    
    def make_order_recommendation(self):
        self.__clean_stock_historical_data()
        self.__backtest__()
        prediction = self.__next_prediction__()
        print(prediction)
        if prediction >= 0.5 + self.tolerance:
            return OrderType.BUY_RECOMMENDATION
        elif prediction < 0.5 - self.tolerance:
            return OrderType.SELL_RECOMMENDATION
        return OrderType.HOLD_RECOMMENDATION




    # Check precision of predictions   
    #predictions = backtest(sp500, model, predictors)
    #print(predictions["Predictions"].value_counts())
    #print(precision_score(predictions["Target"], predictions["Predictions"]))


