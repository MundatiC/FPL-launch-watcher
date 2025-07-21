# 🕵️‍♂️ Fantasy Premier League Launch Watcher

Monitors the [Fantasy Premier League](https://fantasy.premierleague.com) homepage and alerts you via Telegram the moment the game goes live for the new season.

---

## 📦 Features

- Detects the end of the “Game Updating” phase
- Sends real-time alerts via Telegram
- Uses `.env` file to securely store secrets
- Super lightweight and easy to run

---

## ⚙️ GitHub Actions Workflow

This project includes a GitHub Actions workflow to automate running the watcher in the cloud.

- The workflow is defined in [`.github/workflows/fpl-watcher.yml`](.github/workflows/fpl-watcher.yml).
- It runs the watcher script on a schedule (every 3 minutes by default).
- Secrets such as `BOT_TOKEN` and `CHAT_ID` must be set in your repository's **Settings > Secrets and variables > Actions**.

**To use the workflow:**

1. [Fork this repository](https://github.com/yourusername/fpl-launch-watcher/fork).
2. Go to your fork's **Settings > Secrets and variables > Actions**.
3. Add the following secrets:
    - `BOT_TOKEN` — your Telegram bot token
    - `CHAT_ID` — your Telegram chat ID
4. The workflow will run automatically on the defined schedule and send alerts via Telegram when FPL goes live.

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/fpl-launch-watcher.git
cd fpl-launch-watcher
````

---

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Contents of `requirements.txt`:**

```
requests
beautifulsoup4
python-dotenv
```

---

### 4. Set Up Telegram Bot & Environment Variables

#### 🔹 Create a Bot

1. Go to [@BotFather](https://t.me/BotFather)
2. Send `/start`, then `/newbot`
3. Follow the prompts to name your bot and get your **bot token**

#### 🔹 Get Your Chat ID

1. Open [@userinfobot](https://t.me/userinfobot)
2. Send `/start`
3. Note your Telegram user ID (e.g. `987654321`)

#### 🔹 Use the Provided `.env.example` File

A `.env.example` file is included in the repo to show which environment variables are needed. To set up your own secrets:

1. Copy `.env.example` to a new file named `.env` in the project root:

    ```bash
    cp .env.example .env
    # On Windows:
    # copy .env.example .env
    ```

2. Open `.env` and fill in your actual `BOT_TOKEN` and `CHAT_ID`:

    ```
    BOT_TOKEN=your_actual_bot_token
    CHAT_ID=your_actual_chat_id
    ```

❗ **Important:** Do **not** commit your `.env` file. Add this to `.gitignore`:

```
.env
```

---

### 5. Run the Monitor

```bash
python fpl_watcher.py
```

The script checks the FPL site every 15 minutes by default. Once the site goes live, you’ll get a Telegram alert like:

> 🎉 *Fantasy Premier League is LIVE!* Time to register your team: [https://fantasy.premierleague.com](https://fantasy.premierleague.com)

---

## 🧪 Test Your Bot (Optional)

You can manually test your Telegram setup by temporarily adding this line in `fpl_watcher.py`:

```python
send_telegram_alert("✅ Test message: Your FPL bot is working!")
```

Then run:

```bash
python fpl_watcher.py
```

You should receive the test message instantly in Telegram.
Remove the test line afterward to avoid duplicate alerts.

---

## 🛡 License

This project is licensed under the MIT License.
See the [`LICENSE`](LICENSE) file for details.

---

## 🤝 Contributing

Pull requests welcome! You can contribute by:

* Adding Discord, email, or push notifications
* Automating checks via cron or GitHub Actions
* Packaging it for Docker or PyPI
* Translating setup instructions

Fork, improve, and open a PR!

---

## ✨ Credits

Made with 🐍 Python and ❤️
Built to save FPL fanatics from refreshing every 30 seconds.

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
