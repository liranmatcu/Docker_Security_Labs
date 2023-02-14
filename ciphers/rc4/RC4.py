def ksa(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        # key[i % key_length] is the T vector
        S[i], S[j] = S[j], S[i]  # Swap values
    return S


def prga(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Swap values
        K = S[(S[i] + S[j]) % 256]
        yield K


def encrypt(key, plaintext):
    S = ksa(key)
    keystream = prga(S)
    res = []
    for c in plaintext:
        val = ("%02X" % (c ^ next(keystream)))  # XOR and convert to hex
        res.append(val)
    return ''.join(res)



key = b'0123456789abcdef'
plaintext = b'Hello, world!'
ciphertext = encrypt(key, plaintext)
print(ciphertext)