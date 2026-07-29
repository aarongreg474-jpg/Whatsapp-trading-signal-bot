"""
Entry point for Signal Bot #2. Runs ONE scan pass over all configured
pairs, then exits. Same two strategies as bot 1, sends to WhatsApp instead.

Triggered on a schedule by GitHub Actions (every 30 minutes).
Local test run: python main.py
"""

import traceback

from config import PAIRS, TIMEFRAMES
from data_fetcher import fetch_multi_timeframe
from scalp_strategy import evaluate_scalp_signal
from trend_supertrend_strategy import evaluate_trend_supertrend_signal
import whatsapp_alert


def scan_once():
    for pair in PAIRS:
        try:
            tf_data = fetch_multi_timeframe(pair, TIMEFRAMES)
            m1_df = tf_data["trigger"]

            scalp_result = evaluate_scalp_signal(m1_df)
            print(f"{pair:10s} [scalp] ma={scalp_result['ma_direction']:+d} "
                  f"vortex={scalp_result['vortex_direction']:+d} "
                  f"macd={scalp_result['macd_direction']:+d} "
                  f"-> {scalp_result['final_signal']}")

            if scalp_result["direction"] != 0:
                whatsapp_alert.send_scalp_signal(pair, scalp_result)

            trend_result = evaluate_trend_supertrend_signal(m1_df)
            print(f"{pair:10s} [trend]  ma={trend_result['ma_dir']:+d} "
                  f"zigzag={trend_result['zigzag_dir']:+d} "
                  f"supertrend={trend_result['supertrend_dir']:+d} "
                  f"rsi={trend_result['rsi_dir']:+d} "
                  f"-> {trend_result['final_signal']}")

            if trend_result["direction"] != 0:
                whatsapp_alert.send_trend_supertrend_signal(pair, trend_result)

        except Exception as e:
            print(f"[error] {pair}: {e}")
            traceback.print_exc()


if __name__ == "__main__":
    scan_once()
