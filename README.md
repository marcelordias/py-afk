# 🖱️ Anti-Idle Mouse Mover

A simple Python script that moves your mouse cursor in a **circular motion** to prevent inactivity detection — great for keeping your status "active" in Microsoft Teams, Slack, Zoom, etc.

## 🚀 Features

- Moves the mouse in a perfect circle
- Delay controls both speed and radius
- Minimal: no hotkeys, no extra libraries
- Compatible with macOS, Windows, Linux

## 🧩 Requirements

- Python 3.7+
- [`pyautogui`](https://pypi.org/project/pyautogui/)

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🛠️ Usage

Run the script and enter the delay in seconds when prompted:

```bash
python main.py
```

Example input:
```
Enter delay in seconds (e.g., 10): 10
```

- Cursor will move in a smooth circle every 10 seconds
- Press `Ctrl+C` to stop the script

> If you’re on macOS, make sure to **allow control** of your computer in:
>  
> System Settings → Privacy & Security → Accessibility → Enable your terminal app

## 📁 Project Structure

```
anti-idle/
├── main.py
├── requirements.txt
└── README.md
```

## ⚠️ Disclaimer

This script is meant for **personal productivity** only. Do not use it to deceive time-tracking or activity monitoring systems in ways that violate terms of service or workplace policies.

## 📄 License

MIT License — use it freely and responsibly.
