class Decryptor:
    def run(self, b, k):
        return bytes(b[i] ^ k[i % len(k)] for i in range(len(b)))
