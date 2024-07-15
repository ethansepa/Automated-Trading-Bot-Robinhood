import robin_stocks.robinhood as rs

from backend.ml_model.bots.trade_bot import TradeBot
from backend.ml_model.models.rolling_avg_trend_model import RollingAvgTrendModel

def main():

    # Make predictions on top 3 stocks
    rolling_avg_trend_trade_bot = TradeBot(RollingAvgTrendModel())
    '''
    top_100 = rs.markets.get_top_100()
    for stocks in top_100[0:4]:
        print(stocks["symbol"] + ": " + stocks["last_trade_price"])
        print(rolling_avg_trend_trade_bot.check_model(stocks["symbol"]))
    '''
    print("S&P: ")
    print(rolling_avg_trend_trade_bot.trade(amount_in_dollars=1))
    print("SOFI: ")
    print(rolling_avg_trend_trade_bot.trade(amount_in_dollars=1, ticker="SOFI"))
    print("APPLE: ")
    print(rolling_avg_trend_trade_bot.trade(amount_in_dollars=1, ticker="AAPL"))

if __name__ == "__main__":
    main()