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
  
  #shuffle column order from alphabetical to the order of the key [word]
  alphaOrder = ''.join(sorted(key))
  finalciphertext = [''] * len(key)
  for i in range(len(key)):
    for j in range(len(key)):
      if key[i] == alphaOrder[j]:
        finalciphertext[i] = ciphertext[j]
  # read across each column to get the plaintext
  plaintext = ""
  for row in range(blocksize):
    for column in range(keysize):
      plaintext += finalciphertext[column][row]
      #print(ciphertext)
  return plaintext

####################################################################################
# Name: fitness
#
####################################################################################
def fitness(plaintext):
  ptlen = len(plaintext)
  words = ["THE", "MAN", "MEN", "AND", "ING", "ENT", "ION", "HER", "FOR", "ONE", "THIS", "FIGHT", "COUNTRY", "LIBERTY", "DEATH"]
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
def test(plaintext = "THISISASHORTBLOCKOFTEXTTOSEEIFIGOTITRIGHTSNOWFOOBA", key = "4329756180", verbose = True):
  
  ct = encrypt(plaintext, key)
  pt = decrypt(ct, key)

  if verbose:
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
  keys = permutations("0123456789")
  bestkey = ""
  highscore = 0
  for i in list(keys):
    key =  "".join(i)
    pt = decrypt(ciphertext, key)
    score = fitness(pt)
    if score > highscore:
      highscore = score
      bestkey = key
      
  print("high score: ", highscore, "key: ", bestkey)  
  

print("testing solve")

pt = "THISISASHORTBLOCKOFTEXTTOSEEIFIGOTITRIGHTSNOWFOOBA"
key = "5964203178"
ct = encrypt(pt, key)
starttime = time.time()
solve(ct)
endtime = time.time()
print("elapsed time: ", endtime - starttime)
#print("running test")
#test()
