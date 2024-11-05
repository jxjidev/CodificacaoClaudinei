from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def aes_encrypt(plaintext, key):
    # Gera um vetor de inicialização (IV) para o modo CBC
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Realiza o padding para ajustar o texto ao bloco de 128 bits
    padded_text = plaintext + (16 - len(plaintext) % 16) * ' '
    ciphertext = cipher.encrypt(padded_text.encode())
    # Retorna o IV + ciphertext em base64 para facilitar a leitura
    return base64.b64encode(iv + ciphertext).decode()

def aes_decrypt(ciphertext, key):
    # Decodifica o base64
    ciphertext = base64.b64decode(ciphertext)
    # Extrai o IV do início do texto cifrado
    iv = ciphertext[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Descriptografa o texto
    decrypted_text = cipher.decrypt(ciphertext[16:]).decode().rstrip()
    return decrypted_text

# Exemplo de uso do AES:
key = get_random_bytes(16)  # Gera uma chave de 128 bits
plaintext = "Mensagem secreta"
ciphertext = aes_encrypt(plaintext, key)
print("Texto Cifrado (AES):", ciphertext)

decrypted_text = aes_decrypt(ciphertext, key)
print("Texto Decifrado (AES):", decrypted_text)
