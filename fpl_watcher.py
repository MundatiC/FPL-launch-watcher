# Fantasy Premier League Launch Watcher
# -------------------------------------
# Monitors https://fantasy.premierleague.com and alerts you via Telegram when the game goes live.
# License: MIT

import os
import time
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# === Load env variables ===
load_dotenv()

# === CONFIGURATION ===
BOT_TOKEN =  os.getenv("BOT_TOKEN")  # Replace with your Telegram bot token
CHAT_ID = os.getenv("CHAT_ID")      # Replace with your Telegram chat ID


def is_fpl_live():
    url = "https://fantasy.premierleague.com"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 503:
            print("🔧 FPL server returned 503 — still updating...")
            return False
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else ""

        if "Game Updating" in title:
            print("🔄 FPL still updating...")
            return False
        else:
            print("✅ FPL is likely LIVE!")
            return True

    except Exception as e:
        print(f"⚠️ Error checking FPL: {e}")
        return False


def send_telegram_alert(message):
    """
    Send a message via Telegram bot.
    """
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("📬 Telegram alert sent!")
    except Exception as e:
        print(f"⚠️ Failed to send Telegram alert: {e}")


# === MAIN LOOP ===
if __name__ == "__main__":
    print("📡 Starting FPL launch monitor...")
    send_telegram_alert("✅ Test message: Your FPL bot is working!")
    while True:
        if is_fpl_live():
            send_telegram_alert("🎉 *Fantasy Premier League is LIVE!* Time to register your team: https://fantasy.premierleague.com")
        else:
            print("❌ FPL is not live yet.")

