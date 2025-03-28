import ecdsa
import os

if not os.path.exists(r'C:\Users\Administrator\bmttnc-hutech-2280602006\Lab03\Cipher\ecc\keys'):
    os.makedirs(r'C:\Users\Administrator\bmttnc-hutech-2280602006\Lab03\Cipher\ecc\keys')

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        vk = sk.get_verifying_key()
        with open(r'C:\Users\Administrator\bmttnc-hutech-2280602006\Lab03\Cipher\ecc\keys\privatekey.pem', 'wb') as p:
            p.write(sk.to_pem())
        with open(r'C:\Users\Administrator\bmttnc-hutech-2280602006\Lab03\Cipher\ecc\keys\publickey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        with open(r'C:\Users\Administrator\bmttnc-hutech-2280602006\Lab03\Cipher\ecc\keys\privatekey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())
        with open(r'C:\Users\Administrator\bmttnc-hutech-2280602006\Lab03\Cipher\ecc\keys\publickey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())
        return sk, vk

    def sign(self, message, key):
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, key):
        try:
            return key.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False