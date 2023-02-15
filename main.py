#######################################################################################
# Name: encrypt
#######################################################################################
from itertools import permutations
import time

def encrypt(plaintext, key):
    ciphertext = [''] * len(key)
    
    for column in range(len(key)):
      char = column
      while char < len(plaintext):
        ciphertext[column] += plaintext[char]
        char += len(key)
    
    #shuffle columns to be in alphabetical order of the key
    alphaOrder = ''.join(sorted(key))
    finalciphertext = [''] * len(key)
    for i in range(len(key)):
      for j in range(len(key)):
        if alphaOrder[i] == key[j]:
          finalciphertext[i] = ciphertext[j]
    
    return ''.join(finalciphertext)
#######################################################################################
# Name: decrypt
#######################################################################################
def decrypt(ct, key):
  keysize = len(key)
  blocksize = int(len(ct)/keysize) 
  ciphertext = [''] * keysize
  #read blocks of text representing columns
  for block in range(keysize):
    ciphertext[block] = ct[block * blocksize: block * blocksize + blocksize ]
  
  #shuffle columns to be realigned with the key order
  alphaOrder = ''.join(sorted(key))
  finalciphertext = [''] * len(key)
  for i in range(len(key)):
    for j in range(len(key)):
      if key[i] == alphaOrder[j]:
        finalciphertext[i] = ciphertext[j]
        
  # read across each row to get the plaintext
  plaintext = ""
  for row in range(blocksize):
    for column in range(keysize):
      plaintext += finalciphertext[column][row]
  return plaintext


####################################################################################
# Name: fitness
#
####################################################################################
def fitness(plaintext):
  ptlen = len(plaintext)
  words = ["THE", "MAN", "MEN", "AND", "ING", "ENT", "ION", "HER", "FOR", "ONE", "THIS", "FIGHT", "COUNTRY", "LIBERTY", "DEATH", "TEXT", "SNOW"]
  score = 0
  for word in words:
    wordlen = len(word)
    for i in range(ptlen - wordlen):
      snippet = plaintext[i : i + wordlen]
      if snippet == word:
        score += wordlen**2
  return score

####################################################################################
# Name: test
# Description: test the columnar decrypt and encrypt functions
####################################################################################
def test(plaintext = "THISISASHORTBLOCKOFTEXTTOSEEIFIGOTITRIGHTSNOWFOOBA", key = "42031"):
  
  ct = encrypt(plaintext, key)
  pt = decrypt(ct, key)
  
  print("plaintext = ", plaintext)
  print("ct =        ", ct)
  print("pt =        ", pt)
  print("fitness score = ",fitness(pt))
  if plaintext == pt:
    return True
  return False

####################################################################################
# Name: solve
# Description: Solve the Black Hat Challenge for Columnar encoded text with no
#              punctuation and no spaces, all the same case.
# Usage:       solve(ciphtertex, key)
#                cypertext: a string of upper case letters with no spaces
#                key: a string of all ten digits from 0 to 9 in any order
# Output:      writes the top fitness scores and corresponding key value to
#              the file "mostfit.txt" in the current directory
####################################################################################
def solve(ciphertext):
  keys = permutations("01234567")
  bestkey = ""
  highscore = 0
  solved = ""
  for i in list(keys):
    key =  "".join(i)
    pt = decrypt(ciphertext, key)
    score = fitness(pt)
    if score > highscore:
      highscore = score
      bestkey = key
      solved  = pt
      
  print("high score: ", highscore, "key: ", bestkey)
  print(solved)
  

print("testing solve")

pt = "THISISASHORTBLOCKOFTEXTTOSEEIFIGOTITRIGHTSNOWFOOBARLIBERTYMENBAT"
key = "640713528"
ct = encrypt(pt, key)
starttime = time.time()
solve(ct)
endtime = time.time()
print("elapsed time: ", endtime - starttime)

#print("running test")
#test()
