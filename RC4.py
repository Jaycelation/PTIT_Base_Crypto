def KSA(key):
    S = list(range(256))
    j = 0
    key_length = len(key)

    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i] 

    return S

def PRGA(S, data_length):
    i = j = 0
    keystream = []

    for _ in range(data_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  

        K = S[(S[i] + S[j]) % 256] 
        keystream.append(K)

    return keystream

def RC4(key, data):
    S = KSA([ord(c) for c in key])  
    keystream = PRGA(S, len(data))  
    encrypted_data = [data[i] ^ keystream[i] for i in range(len(data))]

    return bytes(encrypted_data)  

key = "secret"  
plaintext = "Hello, RC4!"  
plaintext_bytes = plaintext.encode()  

ciphertext = RC4(key, plaintext_bytes)
print("Ciphertext (hex):", ciphertext.hex())  

decrypted_text = RC4(key, ciphertext)
print("Decrypted:", decrypted_text.decode())