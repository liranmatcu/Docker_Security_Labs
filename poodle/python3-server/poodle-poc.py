#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Poodle attack - PoC
    Implementation of the cryptography behind the attack
    Author: mpgn <martial.puygrenier@gmail.com> - 2016
    Update : 2018 - refactor to python3
'''

import binascii
import sys
import re
import hmac, hashlib, base64
from Crypto.Cipher import AES
from Crypto import Random

"""
    Implementation of AES-256 with CBC cipher mode
    cipher = plaintext + hmac + padding
    IV and KEY are random
    there is no handshake (no need) 
"""

IV = Random.new().read( AES.block_size )
KEY = Random.new().read( AES.block_size )

# generate random key and iv
def randkey():
    global IV 
    IV = Random.new().read( AES.block_size )
    global KEY 
    KEY = Random.new().read( AES.block_size )

# padding for the CBC cipher block
def pad(s):
    return (16 - len(s) % 16) * chr((16 - len(s) - 1) % 16)

# unpad after the decryption 
# return the msg, the hmac and the hmac of msg 
def unpad_verifier(s):
    msg = s[0:len(s) - 32 - ord(s[len(s)-1:]) - 1]
    hash_c = s[len(msg):-ord(s[len(s)-1:]) - 1]
    hash_d = hmac.new(KEY, msg, hashlib.sha256).digest()
    return msg, hash_d, hash_c

# cipher a message
def encrypt( msg):
    data = msg.encode()
    hash = hmac.new(KEY, data, hashlib.sha256).digest()
    padding = pad(data + hash)
    raw = data + hash + padding.encode()
    cipher = AES.new(KEY, AES.MODE_CBC, IV )
    return cipher.encrypt( raw )

# decipher a message then check if padding is good with unpad_verifier()
def decrypt( enc):
    decipher = AES.new(KEY, AES.MODE_CBC, IV )
    plaintext, signature_2, sig_c = unpad_verifier(decipher.decrypt( enc ))

    if signature_2 != sig_c:
        return 0
    return plaintext


'''
    the main attack start here
    the function run(SECRET) will try to decipher the SECRET without knowing the key 
    used for AES
'''

def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

def run(SECRET):
    
    secret = []

    length_block = 16

    a = encrypt(SECRET)
    print(decrypt(a))

    # fill the last block with full padding 0f
    t = binascii.hexlify(encrypt(SECRET))
    original_length = len(t)
    t = 1
    while(True):
        length = len(binascii.hexlify(encrypt("a"*t + SECRET)))
        if( length > original_length ):
            break
        t += 1
    save = t
    v = []

    # we can decipher block_1...block_n-2 => the plaintext
    print("[+] Start Deciphering using POA...")
    for block in range(original_length//32-2,0,-1):
        for char in range(length_block):
            count = 0
            while True:

                randkey()
                request = split_len(binascii.hexlify(encrypt("$"*16 + "#"*t + SECRET + "%"*(block*length_block - char))), 32)
                # change the last block with a block of our choice
                request[-1] = request[block]
                # send the request a get the result => padding error OR OK
                cipher = binascii.unhexlify(b''.join(request).decode())
                plain = decrypt(cipher)
                count += 1

                if plain != 0:
                    t += 1
                    pbn = request[-2]
                    pbi = request[block - 1]
                    # padding is ok we found a byte
                    decipher_byte = chr(int("0f",16) ^ int(pbn[-2:],16) ^ int(pbi[-2:],16))
                    secret.append(decipher_byte)
                    tmp = secret[::-1]
                    sys.stdout.write("\r[+] Found byte \033[36m%s\033[0m - Block %d : [%16s]" % (decipher_byte, block, ''.join(tmp)))
                    sys.stdout.flush()
                    break
        print('')
        secret = secret[::-1]
        v.append(('').join(secret))
        secret = []
        t = save

    v = v[::-1]
    plaintext = re.sub('^#+','',('').join(v))
    print("\n\033[32m{-} Deciphered plaintext\033[0m :", plaintext)
    return v


if __name__ == '__main__':  

    print("{-} Poodle Proof of Concept\n")

    SECRET = "This is a PoC of the Poodle Attack against SSL/TLS"
    print("[+] Secret plaintext :", SECRET)
    print("[+] Encrypted with \033[33mAES-256 MODE_CBC\033[0m")
    print("")
    run(SECRET)
    print("")

    SECRET = "I can decipher the plaintext without knowing the private key used for the encryption"
    print("[+] Secret plaintext :", SECRET)
    print("[+] Encrypted with \033[33mAES-256 MODE_CBC\033[0m")
    print("")
    run(SECRET)   

    print("\n{-} Poodle PoC github.com/mpgn/Poodle-PoC")