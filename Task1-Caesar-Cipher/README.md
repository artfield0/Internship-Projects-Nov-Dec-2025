Task 1 – Caesar Cipher Encryption Tool

This program implements a simple Caesar Cipher, one of the earliest and most basic encryption techniques. It works by shifting each letter in the input text by a fixed number of positions in the alphabet.

🔐 Features

Encrypts text using a shift key

Decrypts encrypted text

Preserves alphabet case (upper/lower)

Ignores non-alphabet characters

Simple logic ideal for learning cryptography basics

▶️ How to Run
Encrypt
python3 caesar_cipher.py --encrypt "HELLO" --shift 3

Decrypt
python3 caesar_cipher.py --decrypt "KHOOR" --shift 3


(If your implementation uses input prompts, adjust accordingly.)

📌 Example

Input:

HELLO
Shift: 3


Output:

KHOOR

📁 Project Structure
Task1-Caesar-Cipher/
├── caesar_cipher.py
└── README.md
