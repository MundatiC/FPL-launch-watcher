# Fantasy Premier League Launch Watcher
# -------------------------------------
# Monitors https://fantasy.premierleague.com and alerts you via Telegram when the game goes live.
# License: MIT

import os
import requests
import cloudscraper
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# === Load env variables ===
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

STATE_FILE = "fpl_live_status.txt"


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

    # === STEP 2: Check homepage title
    try:
        homepage_response = scraper.get(homepage_url, timeout=10)
        html = homepage_response.text

        if "html" in homepage_response.headers.get("Content-Type", ""):
            soup = BeautifulSoup(html, "html.parser")
            title_text = soup.title.string.strip().lower() if soup.title else ""

            if "game updating" in title_text:
                print("🔄 Homepage still says 'Game Updating' – not live.")
                return False
            else:
                print("✅ Homepage title changed – might be live!")
                return True
        else:
            print("✅ Homepage returned non-HTML – assuming live.")
            return True
    except Exception as e:
        print(f"⚠️ Homepage error: {e}")
        return False


def send_telegram_alert(message):
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


def alert_already_sent():
    return os.path.exists(STATE_FILE)


def mark_alert_sent():
    with open(STATE_FILE, "w") as f:
        f.write("sent")


# === MAIN ===
if __name__ == "__main__":
    print("📡 Starting FPL launch monitor...")

    if alert_already_sent():
        print("✅ Alert already sent previously. Exiting.")
    else:
        if is_fpl_live():
            send_telegram_alert("🎉 *Fantasy Premier League is LIVE!* Time to register your team: https://fantasy.premierleague.com")
            mark_alert_sent()
        else:
            print("❌ FPL is not live yet.")
