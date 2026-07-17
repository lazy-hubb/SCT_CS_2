# Image Encryption & Decryption Tool

## 🔐 What This Project Does
A Python program that encrypts images by manipulating every pixel's RGB values using **XOR encryption**. The encryption turns a clear image into static noise. The decryption code reverses the process perfectly!

## 📁 Files
- `encrypt.py` - Encrypts an image (input.jpg → encrypted.jpg)
- `decrypt.py` - Decrypts an image (encrypted.jpg → decrypted.jpg)

## 🖼️ Results
| Image | Description |
| :--- | :--- |
| input.jpg | Original image |
| encrypted.jpg | Scrambled/encrypted image |
| decrypted.jpg | Restored image (matches original perfectly!) |

## 🛠️ How to Run
```bash
python3 encrypt.py
python3 decrypt.py

📚 What I Learned

    Understanding RGB color values

    Pixel manipulation using Pillow library

    XOR encryption (bitwise operations)

    Looping through every pixel in an image

📌 Technologies Used

    Python

    Pillow (PIL) Library
