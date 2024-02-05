import pytest
import robin_stocks.robinhood as rs

from ..src.automatedTradingBotRobinhood import TradeBot

trade_bot = TradeBot()
top_100 = rs.markets.get_top_100()
for stocks in top_100[0:3]:
    print(stocks["symbol"] + ": " + stocks["last_trade_price"])
    print(trade_bot.check_model(stocks["symbol"]))
