import rsa
from rsa import PrivateKey, PublicKey  # Import trực tiếp từ thư viện rsa
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa as crypto_rsa
from cryptography.hazmat.backends import default_backend

if not os.path.exists(r'C:\Users\Administrator\bmttnc-hutech-2280602006\Lab03\Cipher\rsa_cipher\keys'):
    os.makedirs(r'C:\Users\Administrator\bmttnc-hutech-2280602006\Lab03\Cipher\rsa_cipher\keys')

class RSACipher:
    def __init__(self):
        pass

    def generate_keys(self):
        private_key = crypto_rsa.generate_private_key(
            public_exponent=65537,
            key_size=1024,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        with open(r'C:\Users\Administrator\bmttnc-hutech-2280602006\Lab03\Cipher\rsa_cipher\keys\publicKey.pem', 'wb') as p:
            p.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))
        with open(r'C:\Users\Administrator\bmttnc-hutech-2280602006\Lab03\Cipher\rsa_cipher\keys\privateKey.pem', 'wb') as p:
            p.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))

    def load_keys(self):
        with open(r'C:\Users\Administrator\bmttnc-hutech-2280602006\Lab03\Cipher\rsa_cipher\keys\privateKey.pem', 'rb') as p:
            private_key = serialization.load_pem_private_key(
                p.read(),
                password=None,
                backend=default_backend()
            )
        with open(r'C:\Users\Administrator\bmttnc-hutech-2280602006\Lab03\Cipher\rsa_cipher\keys\publicKey.pem', 'rb') as p:
            public_key = serialization.load_pem_public_key(
                p.read(),
                backend=default_backend()
            )
        private_key_rsa = PrivateKey(
            n=private_key.private_numbers().p * private_key.private_numbers().q,
            e=65537,
            d=private_key.private_numbers().d,
            p=private_key.private_numbers().p,
            q=private_key.private_numbers().q
        )
        public_key_rsa = PublicKey(
            n=public_key.public_numbers().n,
            e=public_key.public_numbers().e
        )
        return private_key_rsa, public_key_rsa

    def encrypt(self, message, key):
        return rsa.encrypt(message.encode('ascii'), key)

    def decrypt(self, ciphertext, key):
        try:
            return rsa.decrypt(ciphertext, key).decode('ascii')
        except:
            return False

    def sign(self, message, key):
        return rsa.sign(message.encode('ascii'), key, 'SHA-1')

    def verify(self, message, signature, key):
        try:
            return rsa.verify(message.encode('ascii'), signature, key) == 'SHA-1'
        except:
            return False