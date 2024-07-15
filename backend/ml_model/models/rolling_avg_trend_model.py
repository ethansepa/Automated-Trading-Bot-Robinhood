from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score

import yfinance as yf # calls Yahoo Finance api to download daily stock and index prices
import pandas as pd

from backend.ml_model.models.base_model import BaseModel

class RollingAvgTrendModel(BaseModel):
    def __init__(self, ticker="^GSPC"):
        # Create model
        super().__init__()

    def __create_predictors__(self):
        # Create predictors
        horizons = [2, 5, 60, 250, 1000]

        for horizon in horizons:
            rolling_avgs = self.stock_history.rolling(horizon).mean()

            ratio_col = f"Close_Ratio_{horizon}"
            self.stock_history[ratio_col] = self.stock_history["Close"] / rolling_avgs["Close"]

            trend_col = f"Trend_{horizon}"
            self.stock_history[trend_col] = self.stock_history.shift(1).rolling(horizon).sum()["Target"]
            
            self.predictors += [ratio_col, trend_col]