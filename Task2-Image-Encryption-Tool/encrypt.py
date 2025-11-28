from utils import load_image, save_image
import numpy as np

def encrypt_image(input_path, output_path, key=50):
    img = load_image(input_path)

    # Ensure proper uint8 format
    img = img.astype(np.uint8)

    # 1. Swap Red and Blue channels
    encrypted = img.copy()
    encrypted[:, :, [0, 2]] = encrypted[:, :, [2, 0]]

    # 2. Add key (safe arithmetic using int16)
    encrypted = ((encrypted.astype(np.int16) + key) % 256).astype(np.uint8)

    save_image(output_path, encrypted)
    print("Image encrypted and saved to:", output_path)

if __name__ == "__main__":
    encrypt_image("sample-images/image1.jpg", "encrypted_image.png")
