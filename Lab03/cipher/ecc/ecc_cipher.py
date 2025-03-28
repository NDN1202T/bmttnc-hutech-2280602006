import ecdsa
import os

# Ensure the keys directory exists
if not os.path.exists('week03/cipher/ecc/keys'):
    os.makedirs('week03/cipher/ecc/keys')

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        sk = ecdsa.SigningKey.generate()  # Generate private key
        vk = sk.get_verifying_key()  # Get public key from private key

        # Save private key
        with open('week03/cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())

        # Save public key
        with open('week03/cipher/ecc/keys/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        # Load private key
        with open('week03/cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())

        # Load public key
        with open('week03/cipher/ecc/keys/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())

        return sk, vk

    def sign(self, message, key):
        # Sign data with the private key
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, public_key):
        # Verify the signature using the public key
        try:
            return public_key.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False