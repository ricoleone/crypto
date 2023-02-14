#######################################################################################
# Name: encrypt
#######################################################################################

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
# Name: test
# Description: test the columnar decrypt and encrypt functions
####################################################################################
def test(plaintext = "THISISASHORTBLOCKOFTEXTTOSEEIFIGOTITRIGHTSNOW", key = "mikey"):
  
  ct = encrypt(plaintext, key)
  pt = decrypt(ct, key)
  
  print("plaintext = ", plaintext)
  print("ct =        ", ct)
  print("pt =        ", pt)

  if plaintext == pt:
    return True
  return False

print("run test")
test()
