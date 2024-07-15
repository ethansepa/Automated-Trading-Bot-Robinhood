import yfinance as yf
import pyotp

from backend.ml_model.utilities.order_types import OrderType


    
class TradeBot:
    def __init__(self, model):
        self.model = model

    def trade(self, amount_in_dollars=0, ticker="^GSPC"):
        prediction = self.model.make_order_recommendation()
        if prediction == OrderType.BUY_RECOMMENDATION and self.has_sufficient_funds_available(amount_in_dollars):
            #TODO: send buy order
            return "BUY"
        elif prediction == OrderType.SELL_RECOMMENDATION and self.has_sufficient_equity(ticker):
            #TODO: send sell order
            return "SELL"
        return "HOLD"
    
    def get_current_cash_position():
        return 10
    
    def get_equity_in_position(ticker):
        return 10

    def has_sufficient_funds_available(self, amount_in_dollars):
        """
        Returns a boolean if user's account has enough buying power to execute a buy order.

        :param amount_in_dollars: The amount in USD to be used for a transaction
        :return: True if there are sufficient funds in user's account; False otherwise
        """

        if not amount_in_dollars:
            return False

        # Retrieve the available funds.
        available_funds = self.get_current_cash_position()

        return available_funds >= amount_in_dollars
    
    def has_sufficient_equity(self, ticker, amount_in_dollars):
        """
        Returns a boolean if user's account has enough equity in the given position to execute a sell order.

        :param ticker: A company's ticker symbol as a string
        :param amount_in_dollars: The amount in USD to be used for a transaction
        :return: True if there is sufficient equity in the user's holding; False otherwise
        """

        if not amount_in_dollars or amount_in_dollars <= 0:
            return False

        equity_in_position = self.get_equity_in_position(ticker)

        return equity_in_position >= amount_in_dollars
    
    

