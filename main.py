import robin_stocks.robinhood as rs

from src.automatedTradingBotRobinhood.bots.automated_trading_bot import RollingAvgAndTrendBot

rolling_avg_trend_trade_bot = RollingAvgAndTrendBot()
top_100 = rs.markets.get_top_100()
for stocks in top_100[0:3]:
    print(stocks["symbol"] + ": " + stocks["last_trade_price"])
    print(rolling_avg_trend_trade_bot.check_model(stocks["symbol"]))
