import os
import logging

def generate_key(file_path):
    """Generates a random AES-256 encryption key and saves it."""
    try:
        key = os.urandom(32)  # 256-bit key
        with open(file_path, 'wb') as f:
            f.write(key)

        logging.info(f"🔑 AES-256 key generated and saved at {file_path}")
    except Exception as e:
        logging.error(f"❌ Error generating key: {e}")

def load_key(file_path):
    """Loads the encryption key from the specified file."""
    try:
        with open(file_path, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        logging.error(f"❌ Error: Key file '{file_path}' not found!")
        return None
    except Exception as e:
        logging.error(f"❌ Unexpected error loading key: {e}")
        return None