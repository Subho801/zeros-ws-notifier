<h1 align="center">🎁 Zeros WS Notifier</h1>

<p align="center">
  Lightweight Discord notifier for <strong>Zeros Group</strong> Steam key giveaways using the site's WebSocket API.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![GitHub Actions](https://img.shields.io/github/actions/workflow/status/Subho801/zeros-ws-notifier/notifier.yml?label=Workflow)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

## 📖 About

This project monitors the Zeros Group giveaway platform and automatically sends Discord notifications whenever a Steam key giveaway is announced, goes live, or expires.

Instead of automating a browser with Playwright, it communicates directly with the site's WebSocket endpoint, making it significantly faster and more lightweight.

---

## ✨ Features

- ⚡ Direct WebSocket communication
- 🎮 Official Steam game names via IGDB
- 🟡 Upcoming / 🟢 Live / 🔴 Expired notifications
- 🏆 Featured rewards
- 🔔 Discord webhook support
- 💾 Persistent state to prevent duplicate posts
- 🤖 Automatic GitHub Actions deployment
- 🚀 No browser automation required

---

# 📷 Preview

### Discord Notification

<p align="center">
  <img src="images/embed.png" width="420">
</p>

---

# ⚙️ Requirements

| Requirement | Version |
|------------|---------|
| Python | 3.12+ |
| Discord Webhook | Required |
| Twitch Developer App | Required |
| IGDB API | Required |

---

# 🚀 Installation

```bash
git clone https://github.com/Subho801/zeros-ws-notifier.git

cd zeros-ws-notifier

pip install -r requirements.txt
```

---

# 🔐 Configuration

Create the following environment variables or GitHub Secrets.

| Variable | Required |
|----------|----------|
| DISCORD_WEBHOOK_URL | ✅ |
| TWITCH_CLIENT_ID | ✅ |
| TWITCH_CLIENT_SECRET | ✅ |

---

# ▶️ Run

```bash
python main.py
```

---

# 🧠 How it Works

```
Zeros Group
     │
     ▼
 WebSocket
     │
     ▼
 Giveaway Parser
     │
     ▼
 IGDB Game Lookup
     │
     ▼
 Discord Webhook
```

---

# 📂 Project Structure

```
.
├── .github/
│   └── workflows/
├── discord.py
├── websocket_client.py
├── game_lookup.py
├── igdb.py
├── main.py
├── state.py
├── posted.json
├── game_cache.json
└── requirements.txt
```

---

# 🤝 Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss what you'd like to improve.

---

# ⚠️ Disclaimer

This project is **not affiliated with or endorsed by Zeros Group**.

It is an unofficial community notifier created for educational and automation purposes.

---

# 📄 License

This project is licensed under the MIT License.
