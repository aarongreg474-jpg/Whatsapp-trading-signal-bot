"""
Sends trade signals via WhatsApp using Meta's official WhatsApp Cloud API
(free tier). This requires more one-time setup than Discord/Telegram —
see the README in this folder for the full walkthrough.

Key difference from Discord/Telegram: WhatsApp requires messages sent
outside a live conversation to use a pre-approved "template" (Meta reviews
and approves the wording in advance). You cannot send arbitrary free-form
text the way you can with a webhook or bot token.

This assumes you've created and had approved a template named
"trade_signal" with 4 text placeholders, in this order:
  {{1}} = action (BUY/SELL)
  {{2}} = pair
  {{3}} = candle timeframe
  {{4}} = expiry
"""

import requests
from config import WHATSAPP_ACCESS_TOKEN, WHATSAPP_PHONE_NUMBER_ID, WHATSAPP_RECIPIENT_NUMBER

GRAPH_API_URL = f"https://graph.facebook.com/v20.0/{{phone_number_id}}/messages"


def send_whatsapp_message(action: str, pair: str, candle_timeframe: str, expiry: str):
    url = GRAPH_API_URL.format(phone_number_id=WHATSAPP_PHONE_NUMBER_ID)
    headers = {
        "Authorization": f"Bearer {WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": WHATSAPP_RECIPIENT_NUMBER,
        "type": "template",
        "template": {
            "name": "trade_signal",
            "language": {"code": "en_US"},
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": action},
                        {"type": "text", "text": pair},
                        {"type": "text", "text": candle_timeframe},
                        {"type": "text", "text": expiry},
                    ],
                }
            ],
        },
    }
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"[whatsapp] failed to send message: {e} | response: {getattr(e, 'response', None) and e.response.text}")


def send_scalp_signal(pair: str, result: dict):
    action = "BUY" if result["direction"] == 1 else "SELL"
    send_whatsapp_message(action, pair, "M1", "1 min")


def send_trend_supertrend_signal(pair: str, result: dict):
    action = "BUY" if result["direction"] == 1 else "SELL"
    send_whatsapp_message(action, pair, "M1", "3 min")
