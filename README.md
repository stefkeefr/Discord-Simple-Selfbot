# 🔧 Discord Selfbot

A powerful selfbot for Discord, made for personal use and utility. This bot uses the official Discord API (user token required) and is packed with fun, moderation, and utility features. ⚡

> **⚠️ DISCLAIMER:** This selfbot is against Discord's Terms of Service. Use at your own risk.  
> I am not responsible for any misuse or consequences resulting from this project.

---

## ✨ Features

- `,ping` – Show bot latency
- `,spam <count> <message>` – Spam a message (max 30 times)
- `,setltc <address>` – Set your LTC wallet address
- `,ltc` – Show your LTC address
- `,autoreact <user_id> <emoji>` – Auto-react to messages from a specific user
- `,reactoff` – Disable auto-react
- `,userinfo <@mention or ID>` – Get basic user info
- `,snipe` – View the last deleted message in the channel
- `,typing` – Start fake typing in the current channel
- `,stoptyping` – Stop fake typing
- `,purge <count>` – Delete your own messages
- `,dm <user_id> <message>` – Send a direct message to any user
- `,cmds` – List of all available commands

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.8+
- Required libraries (install with pip):
  ```bash
  pip install discord.py
  pip install discord.py==1.7.3
  pip install colorama

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

### 🔐 Setup

- Clone the repo:

git clone https://github.com/stefkeefr/Discord-Simple-Selfbot
cd selfbot

- Open main.py and paste your Discord token:

token = "YOUR_TOKEN_HERE"

- Run the bot:

python main.py

### 💡 Example Usage

,purge 10
- Bot will delete your last 10 messages from that DM

### ❗ Warning
Using selfbots on Discord is strictly against the Discord Terms of Service, and can result in your account being permanently banned.
This project is for educational purposes only. Use responsibly and at your own risk.
