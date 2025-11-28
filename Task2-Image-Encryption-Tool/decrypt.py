from utils import load_image, save_image
import numpy as np

def decrypt_image(input_path, output_path, key=50):
    img = load_image(input_path)

    # Ensure proper uint8 format
    img = img.astype(np.uint8)

    # Reverse arithmetic
    decrypted = ((img.astype(np.int16) - key) % 256).astype(np.uint8)

    # Swap back channels
    decrypted[:, :, [0, 2]] = decrypted[:, :, [2, 0]]

    save_image(output_path, decrypted)
    print("Image decrypted and saved to:", output_path)

if __name__ == "__main__":
    decrypt_image("encrypted_image.png", "decrypted_image.png")
