# CipherSpeak 🔐

CipherSpeak is a lightweight, terminal-based Python application that allows you to encrypt and decrypt text using a custom symbol-substitution cipher. It converts standard English text into a complex matrix of symbols, making it unreadable to the naked eye, and provides an exact decryption method to revert it back to normal text.

---

## ✨ Features

* **Instant Encryption:** Converts standard alphabetical characters (`a-z`) into custom-mapped symbol strings.
* **Smart Decryption:** Features an automated sorting algorithm that accurately translates complex symbol combinations back into plain text without corruption.
* **Interactive CLI:** A simple, loop-based terminal menu makes it easy to encrypt, decrypt, and exit seamlessly.
* **Error-Resistant:** Handles custom backslash escapes safely to prevent Python syntax warnings.

---

## 🚀 How It Works

The tool maps standard letters to unique symbol configurations. For example:
* `a` becomes `@`
* `w` becomes `\/\/`
* `z` becomes `-/_`

### Encryption Example
* **Input:** `hello world`
* **Output:** `#!^!_!_* \/\/or!_@!`

---

## 🛠️ Installation & Setup

### Prerequisites
* **Python 3.10 or higher** installed on your system.

### Running the Script
1. Clone or download the repository to your local machine.
2. Open your terminal or command prompt and navigate to the directory containing `textsecurity.py`.
3. Run the script using Python:

```bash
python textsecurity.py
```

## 🎮 Usage
When you run the application, you will be greeted with an interactive menu:
```
1. Encrypt text
2. Decrypt text
3. Exit
Enter your choice:
```

* Press 1 to input a plain text string and receive its encrypted symbol counterpart.
* Press 2 to paste encrypted symbols and instantly reveal the original message.
* Press 3 to safely close the program.
