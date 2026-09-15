import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32
ITERATIONS = 600_000


def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS
    )

    return kdf.derive(password.encode())


def encrypt_message(message, password):
    salt = os.urandom(SALT_SIZE)
    nonce = os.urandom(NONCE_SIZE)

    key = derive_key(password, salt)

    aes = AESGCM(key)

    encrypted = aes.encrypt(
        nonce,
        message.encode(),
        None
    )

    return salt + nonce + encrypted


def decrypt_message(data, password):
    salt = data[:SALT_SIZE]

    nonce = data[
        SALT_SIZE:
        SALT_SIZE + NONCE_SIZE
    ]

    encrypted = data[
        SALT_SIZE + NONCE_SIZE:
    ]

    key = derive_key(password, salt)

    aes = AESGCM(key)

    decrypted = aes.decrypt(
        nonce,
        encrypted,
        None
    )

    return decrypted.decode()