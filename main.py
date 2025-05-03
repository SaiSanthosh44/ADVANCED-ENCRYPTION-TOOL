import os
import logging
from modules.encryption import encrypt_file, decrypt_file
from modules.key_manager import generate_key, load_key

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def display_menu():
    """Displays menu options."""
    print("\n🔐 Advanced Encryption Tool")
    print("---------------------------")
    print("1️⃣ Encrypt a File")
    print("2️⃣ Decrypt a File")
    print("3️⃣ Generate New Encryption Key")
    print("4️⃣ Exit")
    return input("\nSelect an option (1-4): ")

def main():
    """Handles user interaction and executes encryption operations."""
    key_file = "C:/Users/saisa/Downloads/Task/Task 4/modules/keys/aes_key.key"

    while True:
        choice = display_menu()

        if choice in ["1", "2"]:
            file_path = input("Enter file path: ").strip()

            if not os.path.exists(file_path):
                logging.error("❌ Error: File does not exist.")
                continue

            if not os.path.exists(key_file):
                logging.error("❌ Error: Encryption key file missing. Generate a new key first.")
                continue

            key = load_key(key_file)
            if not key:
                logging.error("❌ Error: Failed to load encryption key.")
                continue

            try:
                if choice == "1":
                    encrypt_file(file_path, key)
                    logging.info(f"✅ Encrypted {file_path} successfully.")
                else:
                    decrypt_file(file_path, key)
                    logging.info(f"🔓 Decrypted {file_path} successfully.")
            except Exception as e:
                logging.error(f"❌ Error during operation: {e}")

        elif choice == "3":
            try:
                generate_key(key_file)
                logging.info("🔑 New encryption key generated successfully!")
            except Exception as e:
                logging.error(f"❌ Error generating key: {e}")

        elif choice == "4":
            logging.info("Exiting Encryption Tool...")
            break
        else:
            logging.warning("❌ Invalid option.")

if __name__ == "__main__":
    main()