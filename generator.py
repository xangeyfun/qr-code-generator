import os
import qrcode
import random


while True:
    # Create "codes" directory if doesnt exist
    if not os.path.exists("codes/"):
        os.mkdir("codes/")

    print("Please enter the value you want to turn into a QR code:")
    data = input("> ").strip()
    if data.lower() in ("exit", "quit"):
        print("Bye!")
        break

    number = random.randint(1, 10000000)
    with open(f"codes/QRCode_{number}.txt", "a") as f:
        f.write(f"QR Code value: {data}")

    qr = qrcode.make(data)
    qr.save(f"codes/QRCode_{number}.png")
    print(f"QR code saved as QRCode_{number}.png!")
    