
from Crypto.Cipher import AES
from itertools import cycle
import codecs
from base64 import b64encode

def XOR(message, key):
  return ''.join(chr(ord(c)^ord(k)) for c,k in zip(message, cycle(key)))

ct = bytes.fromhex('87dd2acb714db44393d8b4b71bdbad7720fbf40d2e34a03a93324cb9c4b97a08')
ct1 = ct[:16]
ct2 = ct[16:]

key = b'andy love simone'
IV  = b''
cipher = AES.new(key, AES.MODE_ECB)

otp2 = cipher.decrypt(ct2)
print(otp2)
print(b64encode(otp2).decode())
XOR(otp2, ct1)
# print(x_1)
