import robin_stocks.robinhood as robinhood #calls robinhood api
import yfinance as yf

import pyotp

from ..models.rolling_avg_trend_model import RollingAvgTrendModel

class RollingAvgTrendBot:
    def __init__(self):
        robinhood.login('email@email.com','password')
        totp  = pyotp.TOTP("My2factorAppHere").now()

    def check_model(self, ticker="^GSPC"):
        model = RollingAvgTrendModel(ticker)
        prediction = model.predict()
        if prediction == "BUY" and self.__have_funds__():
            #TODO: send buy order
            return "BUY"
        elif prediction == "SELL" and self.__is_holding__(ticker):
            #TODO: send sell order
            return "SELL"
        return "HOLD"

    def __have_funds__(self):
        return True
    
    def __is_holding__(self, ticker="^GSPC"):
        return True
    
    def logout():
        robinhood.logout()

