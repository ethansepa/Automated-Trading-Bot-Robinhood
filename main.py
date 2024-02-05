import robin_stocks.robinhood as rs

from automatedTradingBotRobinhood.logic.src.bots.rolling_avg_trend_bot import RollingAvgTrendBot

# Make predictions on top 3 stocks
rolling_avg_trend_trade_bot = RollingAvgTrendBot()
top_100 = rs.markets.get_top_100()
for stocks in top_100[0:4]:
    print(stocks["symbol"] + ": " + stocks["last_trade_price"])
    print(rolling_avg_trend_trade_bot.check_model(stocks["symbol"]))
