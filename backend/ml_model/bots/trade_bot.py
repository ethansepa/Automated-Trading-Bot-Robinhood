import robin_stocks.robinhood as robinhood #calls robinhood api
import yfinance as yf
import pyotp

from backend.ml_model.utilities.login import RobinhoodCredentials, OrderType


    
class TradeBot:
    def __init__(self, model):
        """Logs user into their Robinhood account."""

        robinhood_credentials = RobinhoodCredentials()
        totp = None

        if robinhood_credentials.mfa_code == "":
            print(
                "WARNING: MFA code is not supplied. Multi-factor authentication will not be attempted. If your "
                "Robinhood account uses MFA to log in, this will fail and may lock you out of your accounts for "
                "some period of time."
            )

        else:
            totp = pyotp.TOTP(robinhood_credentials.mfa_code).now()

        robinhood.login(robinhood_credentials.user, robinhood_credentials.password, mfa_code=totp)
        self.model = model

    

    def robinhood_logout(self):
        """Logs user out of their Robinhood account."""

        robinhood.logout()

    def trade(self, amount_in_dollars, ticker="^GSPC"):
        prediction = self.model.predict()
        if prediction == OrderType.Buy and self.has_sufficient_funds_available(amount_in_dollars):
            #TODO: send buy order
            return "BUY"
        elif prediction == OrderType.SELL and self.has_sufficient_equity(ticker):
            #TODO: send sell order
            return "SELL"
        return "HOLD"

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
    
    

