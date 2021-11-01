#Q2) Given a string, write a function to return the number of times a character appears in a string. the character can be the empty string

str = 'The cat jumped over the moon, the moon was filled with aliens, but only on the dark side. My pge bill was as high as the moon, but my ambition is higher, so I dont worry so much about cost'
ct = {}
str = str.lower()
n = 't'

def strsnum(str,n):
  for i in str:
    ct[i] = ct.get(i,0) +1 

  return ct[n]


strsnum(str,n)
