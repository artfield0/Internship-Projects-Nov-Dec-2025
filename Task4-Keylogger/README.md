# Task 4 – Basic Keylogger (Educational Use Only)

This task demonstrates a simple educational keylogger that records keystrokes
and logs them into a text file. It is designed strictly for learning cybersecurity
concepts such as monitoring, detection, and understanding how keyloggers work.

---

## ⚠️ Legal Notice
This tool must be used **ONLY** on your own device for learning purposes.
Unauthorized use on any device you do not own is illegal.

---

## 🧩 What This Keylogger Does
- Records every key the user presses
- Saves keystrokes into `keylogs.txt`
- Creates a timestamp for every session
- Stops securely when the **ESC key** is pressed
- Captures special keys like:
  - `[Key.enter]`
  - `[Key.space]`
  - `[Key.backspace]`

---
📁 Folder Structure
Task4-Keylogger/
│
├── keylogger.py      # Main program
├── keylogs.txt       # Recorded logs
└── README.md         # Documentation

✔ Purpose of This Task

This tool helps understand:

How keyboard hooks work

How attackers capture keystrokes

How to detect keylogging activity

How anti-malware tools identify suspicious behavior

This knowledge builds strong defensive cybersecurity skills.

## ▶️ How to Run the Keylogger

### **1. Install required package**
```bash
pip install pynput

If your system blocks pip, use:

pip install pynput --break-system-packages

2. Run the keylogger
python3 keylogger.py

3. How to Stop Logging

Press:

ESC


The keylogger will stop immediately and append:

--- Session Ended ---
