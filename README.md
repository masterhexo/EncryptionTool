# Encryption Tool
Created by: Jay Mali  
Telegram: @jaymali841  
Date: Wednesday, February 12, 2025  

---

## What Does This Tool Do?

This tool allows you to securely encrypt and decrypt files using AES encryption (via Python’s `cryptography` library). It ensures that sensitive data remains unreadable without the correct decryption key.

---

## Why Is This Tool Useful?

- Protects sensitive data from unauthorized access.
- Ensures confidentiality in case files are intercepted or stolen.
- Demonstrates practical knowledge of encryption for cybersecurity students.

---

## How to Use This Tool

1. **Generate a Key**:  
   Run the script and select Option `1`. This creates a secure encryption key (`key.key`) required for both encryption and decryption.

2. **Encrypt a File**:  
   Select Option `2` and provide the path of the file you want to encrypt (e.g., `test.txt`). The tool creates an encrypted version of the file (e.g., `test.txt.enc`).

3. **Decrypt a File**:  
   Select Option `3` and provide the path of an encrypted file (e.g., `test.txt.enc`). The tool restores its original content in a new file (e.g., `test.txt`).

4. **Exit**:  
   Select Option `4` to exit.

---

## Important Notes:

- Keep your encryption key (`key.key`) safe! Without it, you cannot decrypt your files.
- Do not modify or edit `.enc` files manually; this may corrupt them.
- Always verify that decryption works before deleting original files.

---

Thank you for using this tool!  
For any questions or feedback, reach out on Telegram at @jaymali841.
