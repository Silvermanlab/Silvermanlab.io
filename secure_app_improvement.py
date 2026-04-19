

import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# -------------------------
# INPUT VALIDATION
# -------------------------
def validate_user_input(data):
    if not data:
        raise ValueError("Input cannot be empty")

    if len(data) > 100:
        raise ValueError("Input too long")

    return True


# -------------------------
# SHA-256 HASHING
# -------------------------
def secure_hash(data):
    validate_user_input(data)
    return hashlib.sha256(data.encode()).hexdigest()


# -------------------------
# AES ENCRYPTION
# -------------------------
def encrypt_sensitive_data(data):
    validate_user_input(data)

    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC)

    encrypted = cipher.encrypt(pad(data.encode(), AES.block_size))

    return key, cipher.iv, encrypted


def decrypt_sensitive_data(key, iv, encrypted):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)

    return decrypted.decode()


# -------------------------
# SIMULATED SECURE COMMUNICATION
# -------------------------
def secure_connection_demo():
    print("Secure connection established using HTTPS protocol simulation.")
