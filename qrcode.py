import cv2
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("qr.png")  # zurag neeh
result = decode(img)

for i in result:
    print("QR кодоос уншсан линк:", i.data.decode("utf-8"))