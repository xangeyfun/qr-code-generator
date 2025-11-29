import os
import qrcode
from datetime import datetime

print("QR Code Generator")
while True:
    # Create "codes" directory if doesnt exist
    if not os.path.exists("codes/"):
        os.mkdir("codes/")

    print("Type any text or URL to create a QR code.")
    print("Type 'exit' or 'quit' to stop.")

    data = input("> ").strip()
    if data.lower() in ("exit", "quit"):
        print("Bye!")
        break

    number = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"codes/QRCode_{number}.txt", "a") as f:
        f.write(f"QR Code value:\n {data}")
    try:
        qr = qrcode.make(data)
        qr.save(f"codes/QRCode_{number}.png")
        qr.show()
        print(f"QR code saved as QRCode_{number}.png!")
    except Exception as e:
        print(f"Failed to create QR code: {e}")
        break