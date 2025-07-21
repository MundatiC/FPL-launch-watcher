# Fantasy Premier League Launch Watcher
# -------------------------------------
# Monitors https://fantasy.premierleague.com and alerts you via Telegram when the game goes live.
# License: MIT

import os
import time
import requests
import cloudscraper
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# === Load env variables ===
load_dotenv()

# === CONFIGURATION ===
BOT_TOKEN =  os.getenv("BOT_TOKEN")  # Replace with your Telegram bot token
CHAT_ID = os.getenv("CHAT_ID")      # Replace with your Telegram chat ID


def is_fpl_live():
    api_url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    homepage_url = "https://fantasy.premierleague.com"
    scraper = cloudscraper.create_scraper()

    # === STEP 1: Try hitting the API ===
    try:
        print("📡 Checking FPL API...")
        api_response = scraper.get(api_url, timeout=10)
        if api_response.status_code == 200 and "application/json" in api_response.headers.get("Content-Type", ""):
            print("✅ FPL API is live!")
            return True
        else:
            print(f"🔄 FPL API returned {api_response.status_code} – falling back to homepage...")
    except Exception as e:
        print(f"⚠️ API error: {e} – falling back to homepage...")

    # === STEP 2: Check the homepage ===
    try:
        homepage_response = scraper.get(homepage_url, timeout=10)
        html = homepage_response.text  # Don't raise_for_status – we still want to inspect 503 pages

        content_type = homepage_response.headers.get("Content-Type", "")
        if "html" in content_type:
            soup = BeautifulSoup(html, "html.parser")
            title_text = soup.title.string.strip().lower() if soup.title else ""

            if "game updating" in title_text:
                print("🔄 Homepage title still says 'Game Updating' – not live.")
                return False
            else:
                print("✅ Homepage no longer shows 'Game Updating' – might be live!")
                return True
        else:
            print("✅ Homepage returned non-HTML (e.g., JSON) – assuming live.")
            return True

    except Exception as e:
        print(f"⚠️ Homepage error: {e}")
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

