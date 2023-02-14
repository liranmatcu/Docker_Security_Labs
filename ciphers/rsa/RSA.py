"""
Implementation of the RSA algorithm
for class demo
"""

import random
import sys
import math

from random import randrange

# The Miller–Rabin primality test is an algorithm 
# which determines whether a given number is prime.
def rabinMiller(n, k = 10):
    if n == 2:
            return True
    if not n & 1:
            return False

    def check(a, s, d, n):
            x = pow(a, d, n)
            if x == 1:
                    return True
            for i in range(1, s - 1):
                    if x == n - 1:
                            return True
                    x = pow(x, 2, n)
            return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
            d >>= 1
            s += 1

    for i in range(1, k):
            a = randrange(2, n - 1)
            if not check(a, s, d, n):
                    return False
    return True

def isPrime(n):
     #lowPrimes is all primes (sans 2, which is covered by the bitwise and operator)
     #under 1000. taking n modulo each lowPrime allows us to remove a huge chunk
     #of composite numbers from our potential pool without resorting to Rabin-Miller
     lowPrimes =   [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
                   ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
                   ,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
                   ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
                   ,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
                   ,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
                   ,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
                   ,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
                   ,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
                   ,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
     if (n >= 3):
         if (n&1 != 0):
             for p in lowPrimes:
                 if (n == p):
                    return True
                 if (n % p == 0):
                     return False
             return rabinMiller(n)
     return False

def generateLargePrime(k):
     #k is the desired bit length
     r = 100*(math.log(k,2)+1) #number of attempts max
     r_ = r
     while r>0:
        # randrange is a twister and is completely deterministic
        # unusable for serious crypto purposes
         n = random.randrange(2**(k-1),2**(k))
         r -= 1
         if isPrime(n) == True:
             return n

     str_failure = "Failure after" + str(r_) + "tries."
     return str_failure


def gcd(a, b):
    '''
    Euclid's algorithm for determining the greatest common divisor
    Use iteration to make it faster for larger integers
    '''
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(a, b):
    """Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb
    """
    # r = gcd(a,b) i = multiplicative inverse of a mod b
    #      or      j = multiplicative inverse of b mod a
    # Neg return values for i or j are made positive mod b or a respectively
    # Iterative Version is faster and uses much less stack space
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a  # Remember original a/b to remove
    ob = b  # negative values from return results
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # If neg wrap modulo original b
    if ly < 0:
        ly += oa  # If neg wrap modulo original a
    # return a , lx, ly  # Return only positive values
    return lx

def rwh_primes2(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

def multiply(x, y):
    _CUTOFF = 1536
    if x.bit_length() <= _CUTOFF or y.bit_length() <= _CUTOFF:  # Base case
        return x * y
    else:
        n = max(x.bit_length(), y.bit_length())
        half = (n + 32) // 64 * 32
        mask = (1 << half) - 1
        xlow = x & mask
        ylow = y & mask
        xhigh = x >> half
        yhigh = y >> half

        a = multiply(xhigh, yhigh)
        b = multiply(xlow + xhigh, ylow + yhigh)
        c = multiply(xlow, ylow)
        d = b - a - c
        return (((a << half) + d) << half) + c


def generate_keypair(keySize=10):

    choice = input("Do you want to enter two prime numbers p and q? [y/n] ")
    if choice == "y" or choice == "Y":
        p = int(input("Enter p: "))
        q = int(input("Enter q: "))
    else:
        print("p and q are auto generated as follows")
        p = generateLargePrime(keySize)
        print("The p value is:", p)
        q = generateLargePrime(keySize)
        print("The q value is:", q)

    if p == q:
        raise ValueError('p and q cannot be equal')

    # n = p*q
    n = multiply(p, q)
    print("The n (i.e., p*q) value is:", n)

    # Phi is the totient of n
    phi = multiply((p-1),(q-1))
    print("The phi(n) value, totient of n, is:", phi)

    #Choose an integer e such that e and phi(n) are co-prime
    if choice == "y" or choice == "Y":
        print("Since you have entered p and q. You can select e.")
        e = int(input("Enter e: "))
    else:
        e = random.randrange(1, phi)
        print("The e value is:", e)

    #Use Euclid's Algorithm to verify that e and phi(n) are co-prime
    g = gcd(e, phi)

    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    print("The d value is:", d)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    print("The enc calculation of each character is as follows")
    i = 0
    for char in plaintext:
        print(char, "=", ord(char))
        print(ord(char), "^", key, "%", n, "=", cipher[i])
        i += 1
    # print(cipher)
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    i = 0
    for char in ciphertext:
        print(char, "^", key, "%", n, "=", ord(plain[i]))
        i += 1
    #Return the array of bytes as a string
    return ''.join(plain)

def main():
    
    print("RSA Encryption and Decryption Demo")

    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair()
    print("Your public key (e, n) is:", public)
    print("Your private key (d, n) is:", private)
    print()

    # Get the message from the user
    if (len(sys.argv) == 2):
        message = str(sys.argv[1])
    else:
        message = input("Please enter your message: ")

    print("Signature Creation and Verification")

    print("Encrypting message with private key (d, n)", private ,"...")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is:")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print()

    print("Decrypting ciphertext with public key (e, n)", public ,"...")
    print("Your decrypted message is:")
    print(decrypt(public, encrypted_msg))
    
if __name__ == "__main__":
    '''
    If the script is being run directly by the user
    '''
    main()
