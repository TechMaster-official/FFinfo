# ✦ TECH MASTER — FF INFO TOOL ✦

> A premium Free Fire account information lookup tool with a colorful, professional terminal UI.
> Designed for **Termux**, Linux, and Windows.

---

## 📌 Overview

**TECH MASTER** is a fast, lightweight Python CLI tool that fetches Free Fire player account information from the public FF Info API and renders it inside a beautifully styled terminal dashboard — gradient banners, card-style fields, animated loaders, and rich color cues.

> **Note:** All existing third-party branding has been removed. This tool is now published under the **TECH MASTER** name.

---

## ✨ Features

| | Feature |
|---|---|
| 🎨 | Rainbow gradient ASCII banner |
| 🪪 | Card-style data display with field icons |
| 🔄 | Animated spinner during API requests |
| 📊 | Auto-formatted numbers, booleans, nested objects |
| 🌐 | Works on **Termux**, Linux & Windows |
| ⚡ | Auto-installs missing dependencies on first run |
| 🛡 | Robust error handling (timeout / 404 / connection) |
| 🔁 | Loop-mode for looking up multiple UIDs |

---

## 📷 Preview

```
   ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆
 _______        ______   __  __    __  __    __  __
/_  __(_)___   /_  __/  / / / /   / / / /   / / / /
 / / / / __ \   / /    / /_/ /   / /_/ /   / /_/ /
/ / / / /_/ /  / /    / __  /   / __  /   / __  /
/_/ /_/\____/  /_/    /_/ /_/   /_/ /_/   /_/ /_/

★  FREE  FIRE  ACCOUNT  INTELLIGENCE  TOOL  ★
v2.0  ✦  PREMIUM  EDITION
   ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆ ◆

➤ Author : T E C H  M A S T E R   |   ➤ Platform : Termux / Linux / Windows
```

---

## 🚀 Installation

### 📱 Termux (Android)

```bash
pkg update -y
pkg install python git -y
git clone https://github.com/TechMaster-official/FFinfo.git
cd FFinfo
python tech-master.py
```

> `requests` will be auto-installed on the first run. If it fails, run:
> ```bash
 pip install requests
> ```

### 🐧 Linux / 🍎 macOS

```bash
git clone https://github.com/TechMaster-official/FFinfo.git
cd FFinfo
python3 -m pip install -r requirements.txt
python3 tech-master.py
```

### 🪟 Windows

```bat
git clone https://github.com/TechMaster-official/FFinfo.git
cd FFinfo
pip install -r requirements.txt
python tech-master.py
```

---

## ▶️ Usage

```bash
python tech-master.py
```

You will be prompted to enter:

| Field   | Example Value | Description |
|---------|---------------|-------------|
| `UID`   | `1234567890`  | The player's Free Fire UID |
| `REGION`| `BD`          | Server region code (e.g. `BD`, `IND`, `NA`, `EU`) |

The tool will then fetch and render the account dashboard in a colorful, easy-to-read layout.

---

## 📂 Project Structure

```
tech-master/
├── tech-master.py     # Main script (premium UI)
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

---

## ⚙️ Requirements

* Python **3.7+**
* Internet connection
* Terminal that supports **ANSI escape codes** (Termux, modern Linux terminals, Windows Terminal — *not legacy `cmd.exe`*)

> 💡 If colors look broken in Windows CMD, use **Windows Terminal** or run via **Git Bash**.

---

## 🛠 Troubleshooting

| Problem | Fix |
|---------|-----|
| `requests` not installing | Run `pip install requests` manually |
| Colors not visible | Use a modern terminal (Windows Terminal / Termux / iTerm2) |
| `Timeout` | Check internet connection; API may be rate-limited |
| `404` on valid UID | Try a different `REGION` code |

---

## 📜 Disclaimer

This tool uses a public, third-party API to fetch publicly available Free Fire account data.
It is intended for **educational and personal use only**.
The author is **not affiliated with Garena or Free Fire**. All trademarks belong to their respective owners.

---

## 🌟 Credits

* Tool name & design: **TECH MASTER**
* Data source: public FF Info API
* Built with ❤️ for the community

---

✦ *Made with TECH MASTER — premium tools for premium users.* ✦
