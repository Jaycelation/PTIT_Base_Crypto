from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# --- 1. Tạo khóa riêng & công khai cho Client ---
client_private_key = ec.generate_private_key(ec.SECP256R1())  # Dùng curve SECP256R1
client_public_key = client_private_key.public_key()

# --- 2. Tạo khóa riêng & công khai cho Server ---
server_private_key = ec.generate_private_key(ec.SECP256R1())
server_public_key = server_private_key.public_key()

# --- 3. Tạo Shared Secret ---
client_shared_secret = client_private_key.exchange(ec.ECDH(), server_public_key)
server_shared_secret = server_private_key.exchange(ec.ECDH(), client_public_key)

# --- 4. Kiểm tra xem khóa chia sẻ có giống nhau không ---
assert client_shared_secret == server_shared_secret  # Chúng phải giống nhau
print("Shared Secret (Hex):", client_shared_secret.hex())

# --- 5. Chuyển đổi khóa chia sẻ thành khóa AES ---
import hashlib
session_key = hashlib.sha256(client_shared_secret).digest()
print("Session Key (SHA-256):", session_key.hex())
