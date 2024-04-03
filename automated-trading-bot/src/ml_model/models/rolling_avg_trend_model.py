from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
import yfinance as yf # calls Yahoo Finance api to download daily stock and index prices

import pandas as pd

class RollingAvgTrendModel:
    def __init__(self, ticker="^GSPC"):
        # Create model
        self.model = RandomForestClassifier(n_estimators=200, min_samples_split=50, random_state=1)
        self.stock = yf.Ticker(ticker)
        self.predictors = []


    def __get_historical_data__(self):
        # Get stocks historical data
        self.stock = self.stock.history(period="max")

        # Remove unneccesary collumns in the data
        del self.stock["Dividends"]
        del self.stock["Stock Splits"]

        # Create a Target to train ML Model by comparing if tommorows price is higher than todays model
        self.stock["Tomorrow"] = self.stock["Close"].shift(-1)
        self.stock["Target"] = (self.stock["Tomorrow"] > self.stock["Close"]).astype(int)

        # Remove old data
        self.stock = self.stock.loc["1995-01-01":].copy()
        self.__create_predictors__()
        self.stock.dropna()


    def __create_predictors__(self):
        # Create predictors
        horizons = [2, 5, 60, 250, 1000]

        for horizon in horizons:
            rolling_avgs = self.stock.rolling(horizon).mean()

            ratio_col = f"Close_Ratio_{horizon}"
            self.stock[ratio_col] = self.stock["Close"] / rolling_avgs["Close"]

            trend_col = f"Trend_{horizon}"
            self.stock[trend_col] = self.stock.shift(1).rolling(horizon).sum()["Target"]
            
            self.predictors += [ratio_col, trend_col]

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
        for i in range (start, self.stock.shape[0], step):
            train = self.stock.iloc[0:i].copy()
            test = self.stock.iloc[i:(i+step)].copy()
            predictions = self.__predict__(train, test)
            all_predictions.append(predictions)
        return pd.concat(all_predictions)
    
    def __next_prediction__(self):
        test = self.stock.iloc[-1:].copy()
        pred_prob = self.model.predict_proba(test[self.predictors])[:,1]
        print(pred_prob)
        if pred_prob >= 0.55:
            return "BUY"
        elif pred_prob < 0.45:
            return "SELL"
        return "HOLD"
    
    def predict(self):
        self.__get_historical_data__()
        self.__backtest__()
        return self.__next_prediction__()


    # Check precision of predictions   
    #predictions = backtest(sp500, model, predictors)
    #print(predictions["Predictions"].value_counts())
    #print(precision_score(predictions["Target"], predictions["Predictions"]))


