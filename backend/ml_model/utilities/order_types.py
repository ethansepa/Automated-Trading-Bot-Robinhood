from enum import Enum

class OrderType(Enum):
    BUY_RECOMMENDATION = 1
    HOLD_RECOMMENDATION = 0
    SELL_RECOMMENDATION = -1