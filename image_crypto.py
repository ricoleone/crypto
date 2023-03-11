from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import os
import secrets
#import request

# http = urllib3.PoolManager()
# response = http.request('GET', 'https://vip.udel.edu/crypto/heckert_gnu.png')
# response = request.get()'https://vip.udel.edu/crypto/heckert_gnu.png')
# mobytext = response.data.decode('UTF-8')
# print('Mobytext ', len(mobytext), mobytext[17], )

# onlyletters = ''.join(filter(lambda x: x.isalpha(), mobytext))

# loweronly = onlyletters.upper()

# f = open("jenkins.jpg", 'wb')
# f.write(response.)
# f.close()
#key = bytes.fromhex('4c6bcaccb1ef923e1ddcce50720dbd7dba0f71d84436cc5651e2d040e0ebd9e7')
#key = bytes.fromhex('686176656e7420646563696465642079')
key = b'i love pbcookies'
print(key)
scheme = AES.new(key, AES.MODE_ECB )
print(type(scheme))
# im = Image.open(r"heckert_gnu.png")
# print(im.format, im.size, im.mode)
# print("AES.block_size Bytes = ", AES.block_size)
# print("Image Bytes = ", im.size[0]*im.size[1])
# print("Image Bytes % AES.block_size ", (im.size[0]*im.size[1]) % AES.block_size)
# im.show()
# encim = scheme.encrypt(pad(im.tobytes(), AES.block_size))
# print(encim[:20])
# im.frombytes(encim)
# print(im.size, im.mode)
# #im.save("nu_image.png")
# im.show()
# im.save('output.png')

pim = Image.open(r"encryptedmm.png")
print(pim.format, pim.size, pim.mode)
pim.frombytes(scheme.decrypt(pim.tobytes()))
pim.show()
pim.save("unencryptedmm.png")
# ni = Image.new(pi, im.size)
#print(pi.format, pi.size, pi.mode)


# ciphertext = scheme.encrypt(b'andyrulz')
# print(ciphertext)
# print(scheme.decrypt(ciphertext))
#########################################################################################
# Name: XOR
# Description: returns a bytearray of two hex strings xor'd
# Usage: foo = XOR("0123456789abc", "feeddeadbeef") 
# Author: Rico Leone
# Date: 
#########################################################################################
def XOR(a, b):
    a_barr = bytearray.fromhex(a)
    b_barr = bytearray.fromhex(b)
    return bytearray(x^y for x,y in zip(a_barr, b_barr))

def gen_iv(bits=AES.block_size):
    iv = secrets.token_urlsafe(bits)
    return iv

def gen_key(bits=AES.block_size):
    key = secrets.token_urlsafe(bits)
    return key

def gen_AES(key, mode=AES.MODE_ECB, iv=b''):
    scheme = AES
    if iv == b'':
        scheme = AES.new(key, mode)
    else:
        scheme = AES.new(key, mode, iv)
    return scheme

def gen_AES_lazy(mode=AES.MODE_ECB):
    key = gen_key()
    iv  = gen_iv()
    scheme = AES.new(key, mode, iv) 
    return key, iv, scheme
def main():
    if __name__ == __main__:
        main()