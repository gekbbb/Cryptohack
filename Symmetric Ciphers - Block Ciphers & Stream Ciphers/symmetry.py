import requests
import json
from pwn import *

url = 'http://aes.cryptohack.org/symmetry/'

def encrypted_flag():
    req = requests.get(url + "encrypt_flag/")
    eflag = req.json()['ciphertext']
    return eflag

def encrypt(plain, iv):
    req = requests.get(url + "encrypt/" + plain + "/" + iv + "/")
    res = req.json()['ciphertext']
    return res

ef = encrypted_flag()
iv = ef[:32]
cip = ef[32:]

ret = encrypt(cip, iv)
print(bytes.fromhex(ret))