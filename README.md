# 🕵️‍♂️ Fantasy Premier League Launch Watcher

Monitors the [Fantasy Premier League](https://fantasy.premierleague.com) homepage and alerts you via Telegram the moment the game goes live for the new season.

---

## 📦 Features

- Detects the end of the “Game Updating” phase
- Sends real-time alerts via Telegram
- Uses `.env` file to securely store secrets
- Uses `cloudscraper` to bypass Cloudflare protection
- GitHub Actions support for automated cloud monitoring via external scheduler

---

## ⚙️ GitHub Actions Workflow

This project includes a GitHub Actions workflow to run the watcher in the cloud.

- The workflow is defined in [`.github/workflows/fpl-launch.yml`](.github/workflows/fpl-launch.yml).
- It is designed to be triggered manually or via an external scheduler (like [cron-job.org](https://cron-job.org)).
- Secrets such as `BOT_TOKEN` and `CHAT_ID` must be set in your repository's **Settings > Secrets and variables > Actions**.

### 🔁 External Trigger Setup (Recommended)

To trigger the workflow every few minutes using [cron-job.org](https://cron-job.org):

1. Go to **cron-job.org** and create a new cron job.
2. Set the **URL** to:
```

https://api.github.com/repos/YOUR_USERNAME/YOUR_REPO/actions/workflows/fpl-launch.yml/dispatches

````
3. Use `POST` as the method, and set the request body to:
```json
{
  "ref": "main"
}
````

4. Add headers:

   * `Content-Type: application/json`
   * `Authorization: token YOUR_GITHUB_PAT`

5. Save and set your preferred schedule (e.g. every 6 minutes).

📌 *Make sure your GitHub personal access token (PAT) has `workflow` scope.*

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

### 4. Set Up Your `.env` File

```bash
cp .env.example .env
# Then fill in:
# BOT_TOKEN=your_actual_bot_token
# CHAT_ID=your_actual_chat_id
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

* Send a test message
* Monitor FPL status
* Alert you via Telegram when the game goes live

Example alert:

> 🎉 *Fantasy Premier League is LIVE!* Time to register your team: [https://fantasy.premierleague.com](https://fantasy.premierleague.com)

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

* Discord or email alerts
* Docker support
* JSON diff for change detection
* Alert rate limiting / cooldown handling

---

## ✨ Credits

Built with Python and caffeine ☕
For every FPL addict tired of pressing F5.

---
