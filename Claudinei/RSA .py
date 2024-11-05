from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def rsa_key_generation():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def rsa_encrypt(plaintext, public_key):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    ciphertext = cipher.encrypt(plaintext.encode())
    return base64.b64encode(ciphertext).decode()

def rsa_decrypt(ciphertext, private_key):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted_text = cipher.decrypt(base64.b64decode(ciphertext)).decode()
    return decrypted_text

# Exemplo de uso do RSA:
private_key, public_key = rsa_key_generation()
plaintext = "Mensagem confidencial"
ciphertext = rsa_encrypt(plaintext, public_key)
print("Texto Cifrado (RSA):", ciphertext)

decrypted_text = rsa_decrypt(ciphertext, private_key)
print("Texto Decifrado (RSA):", decrypted_text)
