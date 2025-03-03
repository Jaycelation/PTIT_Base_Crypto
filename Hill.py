import numpy as np

def text_to_matrix(text, size):
    text = text.upper().replace(" ", "")
    while len(text) % size != 0:
        text += 'X'  
    matrix = [ord(c) - ord('A') for c in text]
    return np.array(matrix).reshape(-1, size)

def matrix_to_text(matrix):
    return "".join(chr(int(c) + ord('A')) for c in matrix.flatten())

def mod_inverse_matrix(matrix, mod=26):
    det = int(round(np.linalg.det(matrix))) 
    det_inv = pow(det, -1, mod)  
    matrix_inv = np.round(det_inv * np.linalg.det(matrix) * np.linalg.inv(matrix)).astype(int) % mod
    return matrix_inv

def hill_cipher(text, key_matrix, encrypt=True):
    mod = 26
    matrix = text_to_matrix(text, key_matrix.shape[0])
    if not encrypt:
        key_matrix = mod_inverse_matrix(key_matrix, mod)
    encrypted_matrix = np.dot(matrix, key_matrix) % mod
    return matrix_to_text(encrypted_matrix)

key_matrix = np.array([[3, 3], [2, 5]])

plaintext = "HELP"
ciphertext = hill_cipher(plaintext, key_matrix)
decrypted_text = hill_cipher(ciphertext, key_matrix, encrypt=False)

print(f"Ciphertext: {ciphertext}") 
print(f"Decrypted: {decrypted_text}")  