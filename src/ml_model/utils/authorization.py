import robin_stocks.robinhood as robinhood #calls robinhood api
from login_credentials import LoginInfo

class Authorization():
    def login():
        username = LoginInfo.username
        password = LoginInfo.password
        robinhood.login(username, password)

    def logout():
        robinhood.logout()