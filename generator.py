import os
import qrcode
from datetime import datetime

print("QR Code Generator")
print("Type any text or URL to create a QR code.")
print("Type 'exit' or 'quit' to stop.")
if not os.path.exists("codes/"):
    os.mkdir("codes/")

while True:
    data = input("> ").strip()

    if data.lower() in ("exit", "quit"):
        print("Bye!")
        break

    if len(data) > 4000:
        print("Text too long for QR code (max ~4000 chars). Try shortening it.")
        continue

    number = datetime.now().strftime("%Y%m%d_%H%M%S")

    with open(f"codes/QRCode_{number}.txt", "w") as f:
        f.write(f"QR Code value:\n {data}")

    try:
        qr = qrcode.make(data)
        qr.save(f"codes/QRCode_{number}.png")
        qr.show()
        print(f"QR code saved as QRCode_{number}.png!")
    except Exception as e:
        print(f"Failed to create QR code: {e}")
        break
