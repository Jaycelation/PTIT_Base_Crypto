import numpy as np

class A5_1:
    def __init__(self, key):
        self.R1 = [0] * 19
        self.R2 = [0] * 22
        self.R3 = [0] * 23
        self.load_key(key)

    def load_key(self, key):
        for i in range(64):
            bit = (key >> i) & 1
            self.R1[i % 19] ^= bit
            self.R2[i % 22] ^= bit
            self.R3[i % 23] ^= bit

    def majority(self, x, y, z):
        return (x & y) | (x & z) | (y & z)

    def clock(self):
        maj = self.majority(self.R1[8], self.R2[10], self.R3[10])

        if self.R1[8] == maj:
            new_bit = self.R1[13] ^ self.R1[16] ^ self.R1[17] ^ self.R1[18]
            self.R1 = [new_bit] + self.R1[:-1]

        if self.R2[10] == maj:
            new_bit = self.R2[20] ^ self.R2[21]
            self.R2 = [new_bit] + self.R2[:-1]

        if self.R3[10] == maj:
            new_bit = self.R3[7] ^ self.R3[20] ^ self.R3[21] ^ self.R3[22]
            self.R3 = [new_bit] + self.R3[:-1]

    def get_keystream(self, length):
        keystream = []
        for _ in range(length):
            self.clock()
            keystream.append(self.R1[-1] ^ self.R2[-1] ^ self.R3[-1])
        return keystream

    def encrypt_decrypt(self, data):
        keystream = self.get_keystream(len(data))
        return np.bitwise_xor(data, keystream)


def file_to_binary(filename):
    with open(filename, "rb") as f:
        data = np.frombuffer(f.read(), dtype=np.uint8)
    binary_data = np.unpackbits(data)  
    return binary_data

def binary_to_file(binary_data, filename):
    byte_data = np.packbits(binary_data)
    with open(filename, "wb") as f:
        f.write(byte_data)


# ======== Chạy thử nghiệm ========
key = 0x123456789ABCDEF  # Khóa 64-bit
a5_1 = A5_1(key)

input_file = "File.mp3"
binary_data = file_to_binary(input_file)

ciphertext = a5_1.encrypt_decrypt(binary_data)
binary_to_file(ciphertext, "encrypted.wav")

a5_1 = A5_1(key)  
decrypted = a5_1.encrypt_decrypt(ciphertext)
binary_to_file(decrypted, "decrypted.wav")

# Kiểm tra
print("Giải mã thành công:", np.array_equal(binary_data, decrypted))