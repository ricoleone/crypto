f = open('encrypted.txt','r')
words = [word.strip() for word in f]
f.close()

onlyletters = ''.join(filter(lambda x: x.isalpha(), words))
loweronly = onlyletters.lower()
# we know the key is length 10 so lets look at every 1oth character and cycle through the alphabet until we get the expected sum of the squares of frequncies for the 10 char key
for i in range(10):
  frequency = {}
  for ascii in range(ord('a'), ord('a')+26):
    frequency[chr(ascii)] = float(loweronly.count(chr(ascii)))/len(loweronly)