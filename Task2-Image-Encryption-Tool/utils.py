import cv2

def load_image(path):
    img = cv2.imread(path)
    if img is None:
        raise ValueError("Could not load image at: " + path)
    return img

def save_image(path, img):
    cv2.imwrite(path, img)
