import hashlib, cProfile

f = open('dictionary.txt','r')
words = [word.strip() for word in f]
f.close()

secretHash=hashlib.sha512(bytes("banana", 'UTF-8')).hexdigest()

def checkDictionary(secret):
    return [word for word in words if hashlib.sha512(bytes(word, 'UTF-8')).hexdigest() == secret]

cProfile.run('checkDictionary(secretHash)')