import os
import logging
from Crypto.Cipher import AES

def pad_data(data):
    """Pads data to match AES block size."""
    return data + b' ' * (AES.block_size - len(data) % AES.block_size)

def encrypt_file(file_path, key):
    """Encrypts a file using AES-256."""
    logging.info(f"🔹 Encrypting file: {file_path}")

    with open(file_path, 'rb') as f:
        data = f.read()

    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(pad_data(data))

    with open(file_path + ".enc", 'wb') as f:
        f.write(encrypted_data)

    logging.info(f"✅ Encrypted file saved as {file_path}.enc")

def decrypt_file(file_path, key):
    """Decrypts an AES-256 encrypted file."""
    logging.info(f"🔹 Decrypting file: {file_path}")

    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data).rstrip(b' ')

    decrypted_filename = file_path.replace(".enc", "_decrypted")
    with open(decrypted_filename, 'wb') as f:
        f.write(decrypted_data)

    logging.info(f"🔓 Decrypted file saved as {decrypted_filename}")

if __name__ == "__main__":
    print("🔹 Encryption module loaded successfully!")