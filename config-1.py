"""
Configuration for Signal Bot #2.

Same two strategies as the first bot:
  - scalp_strategy.py: EMA(3/10) + Vortex(10) + MACD(15,27,9), M1, 1-min expiry
  - trend_supertrend_strategy.py: MA(100) + ZigZag + SuperTrend(10,1) + RSI(10), M1, 3-min expiry

Only difference: different pairs, and a separate Discord channel.
"""

import os

TWELVE_DATA_API_KEY = os.environ.get("TWELVE_DATA_API_KEY", "YOUR_TWELVE_DATA_KEY")
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "YOUR_WEBHOOK_URL")

PAIRS = [
    "USD/CAD", "CAD/CHF", "CHF/JPY",
    "EUR/AUD", "EUR/CHF",
]

TIMEFRAMES = {
    "trend": "1h",
    "signal": "5min",
    "trigger": "1min",
}

CANDLE_LOOKBACK = 150

SWING_WINDOW = 3
SWING_LOOKBACK = 60
STRUCTURE_PROXIMITY_PCT = 0.0025

SCALP_EMA_FAST = 3
SCALP_EMA_SLOW = 10
SCALP_VORTEX_PERIOD = 10
SCALP_MACD_FAST = 15
SCALP_MACD_SLOW = 27
SCALP_MACD_SIGNAL = 9
SCALP_MAX_BARS_SINCE_CROSS = 2
SCALP_ATR_VOLATILITY_MULT = 1.5

TREND_MA_PERIOD = 100
ZIGZAG_WINDOW = 3
ZIGZAG_LOOKBACK = 60
SUPERTREND_PERIOD = 10
SUPERTREND_MULTIPLIER = 1.0
TREND_RSI_PERIOD = 10
SUPERTREND_FRESH_BARS = 2
RSI_OVEREXTEND_BARS = 5
TREND_ATR_VOLATILITY_MULT = 1.5

SCAN_INTERVAL_SECONDS = 1800
API_CALL_DELAY_SECONDS = 8
