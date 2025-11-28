# caesar_cipher.py
# Internship Task 1: Caesar Cipher Encryption and Decryption

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only shift letters
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# User interaction
print("=== Caesar Cipher Encryption/Decryption ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print(f"\nEncrypted Message: {encrypted}")
print(f"Decrypted Message: {decrypted}")
