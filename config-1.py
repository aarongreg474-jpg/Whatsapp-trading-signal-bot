"""
Configuration for Signal Bot #2 (WhatsApp notifications).

Same two strategies as the first bot:
  - scalp_strategy.py: EMA(3/10) + Vortex(10) + MACD(15,27,9), M1, 1-min expiry
  - trend_supertrend_strategy.py: MA(100) + ZigZag + SuperTrend(10,1) + RSI(10), M1, 3-min expiry

Only difference: different pairs, and WhatsApp instead of Discord/Telegram.
"""

import os

# ---------------------------------------------------------------
# API CREDENTIALS
# ---------------------------------------------------------------
# Use a SEPARATE Twelve Data account/key from your first bot, so this bot
# has its own full 800/day free budget instead of sharing bot 1's.
TWELVE_DATA_API_KEY = os.environ.get("TWELVE_DATA_API_KEY", "YOUR_TWELVE_DATA_KEY")

# WhatsApp (Meta Cloud API) — see README for full setup steps.
WHATSAPP_ACCESS_TOKEN = os.environ.get("WHATSAPP_ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
WHATSAPP_PHONE_NUMBER_ID = os.environ.get("WHATSAPP_PHONE_NUMBER_ID", "YOUR_PHONE_NUMBER_ID")
WHATSAPP_RECIPIENT_NUMBER = os.environ.get("WHATSAPP_RECIPIENT_NUMBER", "YOUR_WHATSAPP_NUMBER")

# ---------------------------------------------------------------
# MARKETS TO SCAN
# ---------------------------------------------------------------
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

# ---------------------------------------------------------------
# MARKET STRUCTURE SETTINGS (used by trend_supertrend_strategy.py's ZigZag)
# ---------------------------------------------------------------
SWING_WINDOW = 3
SWING_LOOKBACK = 60
STRUCTURE_PROXIMITY_PCT = 0.0025

# ---------------------------------------------------------------
# SCALP STRATEGY SETTINGS (EMA/Vortex/MACD on M1)
# ---------------------------------------------------------------
SCALP_EMA_FAST = 3
SCALP_EMA_SLOW = 10
SCALP_VORTEX_PERIOD = 10
SCALP_MACD_FAST = 15
SCALP_MACD_SLOW = 27
SCALP_MACD_SIGNAL = 9
SCALP_MAX_BARS_SINCE_CROSS = 2
SCALP_ATR_VOLATILITY_MULT = 1.5

# ---------------------------------------------------------------
# TREND/SUPERTREND STRATEGY SETTINGS (M1, 3-min expiry)
# ---------------------------------------------------------------
TREND_MA_PERIOD = 100
ZIGZAG_WINDOW = 3
ZIGZAG_LOOKBACK = 60
SUPERTREND_PERIOD = 10
SUPERTREND_MULTIPLIER = 1.0
TREND_RSI_PERIOD = 10
SUPERTREND_FRESH_BARS = 2
RSI_OVEREXTEND_BARS = 5
TREND_ATR_VOLATILITY_MULT = 1.5

# 5 pairs x 3 timeframes = 15 requests/scan, every 30 min = 720 requests/day
# — under Twelve Data's free 800/day limit (on THIS bot's own separate account).
SCAN_INTERVAL_SECONDS = 1800
API_CALL_DELAY_SECONDS = 8
