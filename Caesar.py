def caesar_cipher(text, key, encrypt=True):
    result = ""
    shift = key if encrypt else -key
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted_text += char  

    return decrypted_text

plaintext = input("Enter plaintext: ")
key = int(input("Enter key: "))
ciphertext = caesar_cipher(plaintext, key)
decrypted_text = caesar_cipher(ciphertext, key, encrypt=False)

print(f"Ciphertext: {ciphertext}")  # KHOOR
print(f"Decrypted: {decrypted_text}")  # HELLO
