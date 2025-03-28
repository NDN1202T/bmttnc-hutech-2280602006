from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import os

class RSACipher:
    def __init__(self, key_size=2048):
        # Define the directory for storing keys
        self.key_dir = "week03/cipher/rsa/keys"
        os.makedirs(self.key_dir, exist_ok=True)  # Create the directory if it doesn't exist
        self.private_key_file = os.path.join(self.key_dir, "private.pem")
        self.public_key_file = os.path.join(self.key_dir, "public.pem")
        self.key_size = key_size

    def generate_keys(self):
        key = RSA.generate(self.key_size)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        with open(self.private_key_file, "wb") as priv_file:
            priv_file.write(private_key)

        with open(self.public_key_file, "wb") as pub_file:
            pub_file.write(public_key)

    def load_keys(self):
        if not os.path.exists(self.private_key_file) or not os.path.exists(self.public_key_file):
            self.generate_keys()

        with open(self.private_key_file, "rb") as priv_file:
            private_key = RSA.import_key(priv_file.read())

        with open(self.public_key_file, "rb") as pub_file:
            public_key = RSA.import_key(pub_file.read())

        return private_key, public_key

    def encrypt(self, message, key):
        cipher = PKCS1_OAEP.new(key)
        encrypted_message = cipher.encrypt(message.encode())
        return encrypted_message

    def decrypt(self, ciphertext, key):
        cipher = PKCS1_OAEP.new(key)
        decrypted_message = cipher.decrypt(ciphertext).decode()
        return decrypted_message

    def sign(self, message, private_key):
        h = SHA256.new(message.encode())
        signature = pkcs1_15.new(private_key).sign(h)
        return signature

    def verify(self, message, signature, public_key):
        h = SHA256.new(message.encode())
        try:
            pkcs1_15.new(public_key).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False