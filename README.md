# QR Code Generator

A simple Python script that generates QR codes from user input and saves them as PNG files.

## Features

- Interactive command-line interface
- Generates QR codes from any text input
- Saves QR codes as PNG files with the current date
- Stores the original data in corresponding text files
- Creates a dedicated `codes/` directory for output files

## Requirements

- Python 3.x
- qrcode library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/xangeyfun/qr-code-generator.git
cd qr-code-generator
```

2. Install the required dependency:
```bash
pip install qrcode
```

## Usage

Run the script:
```bash
python generator.py
```

Follow the prompts:
- Enter any text you want to convert to a QR code
- Type "exit" or "quit" to stop the program

The script will:
- Create a `codes/` directory if it doesn't exist
- Generate a unique filename (QRCode_[date].png)
- Save the QR code as a PNG image
- Save the original data in a corresponding text file

## Example

```
Please enter the value you want to turn into a QR code:
> https://github.com/xangeyfun
QR code saved as QRCode_20251129_150332.png!
```

## Output Files

- PNG files: `codes/QRCode_[date].png`
- Text files: `codes/QRCode_[date].txt` (contains the original data)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
