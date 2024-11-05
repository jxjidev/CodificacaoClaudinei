import hashlib

def sha256_hash(text):
    sha256 = hashlib.sha256()
    sha256.update(text.encode())
    return sha256.hexdigest()

# Exemplo de uso do SHA-256:
plaintext = "Texto para hashing"
hash_result = sha256_hash(plaintext)
print("Hash (SHA-256):", hash_result)
