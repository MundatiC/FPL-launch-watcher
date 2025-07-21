# 🕵️‍♂️ Fantasy Premier League Launch Watcher

Monitors the [Fantasy Premier League](https://fantasy.premierleague.com) homepage and alerts you via Telegram the moment the game goes live for the new season.

---

## 📦 Features

- Detects the end of the “Game Updating” phase
- Sends real-time alerts via Telegram
- Uses `.env` file to securely store secrets
- Uses `cloudscraper` to bypass Cloudflare protection
- GitHub Actions support for automated cloud monitoring

---

## ⚙️ GitHub Actions Workflow

This project includes a GitHub Actions workflow to automate running the watcher in the cloud.

- The workflow is defined in [`.github/workflows/fpl-launch.yml`](.github/workflows/fpl-launch.yml).
- It runs the watcher script on a schedule (every 3 minutes by default).
- Secrets such as `BOT_TOKEN` and `CHAT_ID` must be set in your repository's **Settings > Secrets and variables > Actions**.

**To use the workflow:**

1. [Fork this repository](https://github.com/yourusername/fpl-launch-watcher/fork).
2. Go to your fork's **Settings > Secrets and variables > Actions**.
3. Add the following secrets:
    - `BOT_TOKEN` — your Telegram bot token
    - `CHAT_ID` — your Telegram chat ID
4. The workflow will run automatically and alert you when FPL goes live.

---

## 🚀 Local Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/fpl-launch-watcher.git
cd fpl-launch-watcher
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt` contains:**

```
requests
beautifulsoup4
python-dotenv
cloudscraper
```

### 4. Set Up Your `.env` File

1. Copy `.env.example` to `.env`:

    ```bash
    cp .env.example .env
    # Windows:
    # copy .env.example .env
    ```

2. Fill in your bot credentials:

    ```env
    BOT_TOKEN=your_actual_bot_token
    CHAT_ID=your_actual_chat_id
    ```

---

## 💬 Telegram Setup Guide

### Create a Bot
1. Open [@BotFather](https://t.me/BotFather)
2. Send `/start` then `/newbot`
3. Follow the instructions to get your bot token

### Get Your Chat ID
1. Open [@userinfobot](https://t.me/userinfobot)
2. Send `/start`
3. It will show your Telegram user ID (chat ID)

---

## ▶️ Run the Monitor

```bash
python fpl_watcher.py
```

The script will:
- First test your bot connection
- Then check the API and fallback to the homepage
- Send a Telegram alert when FPL is live

You’ll receive a message like:

> 🎉 *Fantasy Premier League is LIVE!* Time to register your team: https://fantasy.premierleague.com

---

## 🧪 Test Your Bot (Optional)

You can test by running:

```bash
python fpl_watcher.py
```

The first message will be:

> ✅ Test message: Your FPL bot is working!

If you see it, the bot is ready!

---

## 📂 File Structure

```
.
├── fpl_watcher.py
├── .env
├── .env.example
├── LICENSE
├── .gitignore
├── requirements.txt
├── README.md
└── .github
    └── workflows
        └── fpl-launch.yml
```

---

## 🛡 License

MIT — see [`LICENSE`](LICENSE).

---

## 🤝 Contributing

PRs welcome! Ideas for improvement:

- Add Discord, Email, or mobile push notifications
- Docker support
- Early-season change monitoring
- Local JSON snapshot comparison

---

## ✨ Credits

Built with Python and coffee ☕
For every FPL addict tired of pressing F5.

---
