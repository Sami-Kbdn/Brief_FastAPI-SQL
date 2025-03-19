import secrets
import hashlib

# Générer une clé aléatoire avec secrets
secret_key = secrets.token_bytes(32)  # Génère une clé aléatoire de 32 octets

# Appliquer le hash SHA256 sur la clé
hashed_key = hashlib.sha256(secret_key).hexdigest()

print(f"Clé secrète SHA256 : {hashed_key}")