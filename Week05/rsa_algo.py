import random
from hashlib import sha256

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# Function to get gcd of 2 number
def gcd(a: int, n: int):
        return gcd(n, a%n) if n != 0 else a

# Function to change decimal to binary (used for turning the power)
def dec_to_bin(pow):
    bin_list = []
    # 2^0, 2^1, 2^2, ....
    while (pow != 0):
        re = pow % 2
        pow = pow // 2
        bin_list.append(re)
    return bin_list

# Function to solve num^power (mod n)
#simple_mod_list
    # ex: d = 53 = 2^5 + 2^4 + 2^2 + 1
    # 37^(2^0) (mod 77) = 37
    # 37^(2^1) (mod 77) = 37^2 (mod 77) = 60
    # ....
def mod_process(num, power, n):
    power_to_bin : list = dec_to_bin(power)
    simple_mod_list = []
    simple_mod = num % n
    simple_mod_list.append(simple_mod)
    for i in range(1, len(power_to_bin)):
        simple_mod = (simple_mod ** 2) % n
        simple_mod_list.append(simple_mod)
    message = 1
    for k in range(0, len(power_to_bin)):
        if power_to_bin[k] == 1:
            message = (message * simple_mod_list[k]) % n
    return message



# Function to decript a single cybertext(c)
#public key (n, e)
# #private key (n, d) => find d
# p, q are primes
# n = p * q
# z = (p-1)(q-1)
# given e
# find d: ed = 1 mod z
def message_decription(p, q, e, c):
    n = p * q
    z = (p -1) * (q -1)
    d = modinv(e, z)
    return mod_process(c, d % z, n)

def message_encription(p, q, d, m):
    n = p * q
    z = (p - 1) * (q - 1)
    e = modinv(d,z)
    return mod_process(m, e % z, n)

# Function to generate keys using 2 big primes (p, q)
def key_generate(p, q):
    n = p * q
    z = (p - 1) * (q - 1)
    # n, e : pulic key
    # n, d : private key
    while True:
        try:
            e = random.randint(2, z)
            if gcd(e, z) != 1:
                continue
            else:
                break
        except ValueError:
            continue

    d = modinv(e, z)
    return [[n, e], [n, d % z]]



# Function to show the original message given a cyphertext string
# p, q are primes
def rsa_decription(p, q, e, cyphertext: str):
    org_ascii = ''
    org_message = ''
    for x in cyphertext.split():
        org_ascii += str(message_decription(p, q, e, int(x))) + ' '
        org_message += str(chr(message_decription(p, q, e, int(x))))
    print('Original ASCII: ' + org_ascii)
    return org_message

# Function to encrypt an message
def rsa_encription(p, q, d, message: str):
    en_ascii = ''
    for x in message:# ord(x)
        en_ascii += str(message_decription(p, q, d, ord(x))) + ' '
    return en_ascii
    # return ' '.join([str(message_decription(p, q, d, ord(x))) for x in message])


#INCOMPLETE
def signature_generate(message, d, n):
    sig = mod_process(message, d, n)
    return sig

# UPDATING
def signature_vefify(sig, e, n, m):
    return True if mod_process(sig, e, n) == m else False

#
def check_prime(num):
    if num <= 1:
        return False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

def rsa_prog():
    while True:
        try:
            p = int(input('Input a big prime p : '))
            if not check_prime(p):
                print('Not a prime')
                continue
            else:
                break
        except ValueError:
            print('Invalid input! Please re-input')
            continue
    while True:
        try:
            q = int(input('Input a big prime q : '))
            if not check_prime(q):
                print('Not a prime')
                continue
            else:
                break
        except ValueError:
            print('Invalid input! Please re-input')
            continue


    pubk , prik = key_generate(p, q)
    print('Your key: public ({}), private ({})'.format(pubk, prik))
    message = input('Enter a mesage: ')
    org_ascii = ''
    for x in message:
        org_ascii += str(ord(x)) + ' '
    print('Org_ascii from sender: ', org_ascii)


    cypher_text = rsa_encription(p, q, prik[1], message)
    print('Cypher text: ', cypher_text)

    cypher = rsa_decription(p, q, pubk[1], cypher_text)
    print('Message: ', cypher)



rsa_prog()


