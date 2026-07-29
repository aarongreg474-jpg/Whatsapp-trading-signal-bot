# Signal Bot #2 — WhatsApp Edition

Same 2 strategies as bot 1 (EMA/Vortex/MACD scalp + MA/ZigZag/SuperTrend/RSI),
different pairs (USD/CAD, CAD/CHF, CHF/JPY, EUR/AUD, EUR/CHF), sends to
WhatsApp instead of Discord/Telegram.

## Setting up WhatsApp (Meta Cloud API) — the involved part

Unlike Discord/Telegram, WhatsApp requires a few more steps and an approval
wait. Here's the full path:

### 1. Create a Meta Developer account & App
- Go to https://developers.facebook.com/ → log in with a Facebook account
- Create a new App → choose type **"Business"**
- Add the **WhatsApp** product to your app

### 2. Get your test credentials
In your app's WhatsApp → API Setup page, you'll see:
- A **temporary access token** (expires in 24 hours by default — see step 5 for a permanent one)
- A **Phone Number ID** (Meta gives you a free test number)
- Copy both of these

### 3. Add your own number as a test recipient
- Still on the API Setup page, add your real WhatsApp number under "To"
- Meta will text you a verification code — enter it to confirm
- Free tier allows up to 5 verified test recipient numbers

### 4. Create your message template
Free-form text isn't allowed for bot-initiated messages — you need a
pre-approved template:
- Go to **WhatsApp Manager → Message Templates → Create Template**
- Name it exactly: `trade_signal`
- Category: **Utility**
- Body text, using placeholders exactly like this:
  ```
  Signal: {{1}} {{2}}
  Candle: {{3}} | Expiry: {{4}}
  ```
- Submit for review — Meta typically approves within a few hours, sometimes up to 1-2 days

### 5. Get a permanent access token (optional but recommended)
The default token expires every 24 hours, which breaks your automated bot.
To fix this:
- Go to Meta Business Suite → **System Users** → create a new system user
- Assign it your WhatsApp app with full permissions
- Generate a token for that system user — this one doesn't expire

### 6. Add your 3 secrets to GitHub
Once you have your permanent token, phone number ID, and your own WhatsApp
number (with country code, e.g. `2348012345678`), add these as repo secrets:
- `WHATSAPP_ACCESS_TOKEN`
- `WHATSAPP_PHONE_NUMBER_ID`
- `WHATSAPP_RECIPIENT_NUMBER`

Plus your (separate, fresh) Twelve Data key:
- `TWELVE_DATA_API_KEY`

### 7. Test it
Once the template is approved and secrets are added, trigger the workflow
manually from the Actions tab and check your WhatsApp for the message.

## Honest limitation to know about

The free tier restricts you to a small number of verified recipient
numbers (5), and every message must match your approved template's exact
wording pattern — you can't freely change the message format later without
submitting a new template for review each time. This is meaningfully less
flexible than Discord/Telegram, which is why we flagged the tradeoff
upfront.
