import hashlib, bcrypt, random

f = open('dictionary.txt','r')
words = [word.strip() for word in f]
f.close()

salt = bcrypt.gensalt()
index = random.randint(0, len(words) - 1)
secret = words[index]
r = 256

print("The secret is ", secret)
print("The salt value is ", salt)
print("The stretch value is ", r)



def saltStretch(sa, pw, st):
  xi = b'0'
  for i in range(0, st): 
    xi =  hashlib.sha256(xi + bytes(pw, 'UTF-8')  + salt).digest()
  print("K = ", xi)

saltStretch(salt, secret, r)