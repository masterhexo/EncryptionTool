# Encryption Tool
# Created by Jay Mali
# Telegram: @jaymali841
# Date: Wednesday, February 12, 2025

from cryptography.fernet import Fernet
import os

# Ensure the working directory is set correctly
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(f"Working directory set to: {os.getcwd()}")

def generate_key():
    """Generates an encryption key and saves it to 'key.key'."""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as 'key.key'.")

def load_key():
    """Loads the encryption key from 'key.key'."""
    try:
        return open("key.key", "rb").read()
    except FileNotFoundError:
        print("Key file not found! Please generate a key first.")
        return None

def encrypt_file(file_path):
    """Encrypts the specified file using the encryption key."""
    key = load_key()
    if not key:
        return
    fernet = Fernet(key)

    try:
        with open(file_path, "rb") as file:
            file_data = file.read()

        encrypted_data = fernet.encrypt(file_data)

        with open(file_path + ".enc", "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        print(f"File '{file_path}' has been encrypted successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found!")

def decrypt_file(encrypted_file_path):
    """Decrypts the specified encrypted file using the encryption key."""
    key = load_key()
    if not key:
        return
    fernet = Fernet(key)

    try:
        with open(encrypted_file_path, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        original_file_path = encrypted_file_path.replace(".enc", "")
        with open(original_file_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)

        print(f"File '{encrypted_file_path}' has been decrypted successfully.")
    except FileNotFoundError:
        print(f"File '{encrypted_file_path}' not found!")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

if __name__ == "__main__":
    print("=== Encryption Tool ===")
    print("Created by Jay Mali")
    print("Telegram: @jaymali841")

    while True:
        # Display menu options
        print("\n1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            generate_key()
        elif choice == "2":
            file_path = input("Enter the path of the file to encrypt: ").strip()
            encrypt_file(file_path)
        elif choice == "3":
            encrypted_file_path = input("Enter the path of the file to decrypt: ").strip()
            decrypt_file(encrypted_file_path)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
