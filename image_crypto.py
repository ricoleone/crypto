from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import os
import requests

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
key = bytes.fromhex('4c6bcaccb1ef923e1ddcce50720dbd7dba0f71d84436cc5651e2d040e0ebd9e7')
print(key)
salt = b'87654321'
scheme = AES.new(key, AES.MODE_ECB )
im = Image.open(r"jenkins.jpg")
print(im.format, im.size, im.mode)
#im.show()
ci = scheme.encrypt(pad(im.tobytes(), AES.block_size))
print(ci[:20])
#im.save("nu_image.png")
im.show()
f  = open("encrypted.jpg", 'wb')
f.write(ci)
f.close()
f = open("encrypted.jpg", 'rb')
blob = f.read()
print(blob[:20])
pi = unpad(scheme.decrypt(blob), AES.block_size)
# ni = Image.new(pi, im.size)
#print(pi.format, pi.size, pi.mode)


# ciphertext = scheme.encrypt(b'andyrulz')
# print(ciphertext)
# print(scheme.decrypt(ciphertext))