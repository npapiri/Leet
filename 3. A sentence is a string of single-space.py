# Q3)A sentence is a string of single-space separated words where each word consists only of lowercase letters.
   # A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
   # Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

word1 = 'Dogs are smarter than mules, but not as smart as alpacas.'
word2 = 'Sheep dogs are the smartest breed of dogs but not as smart as alpacas.'
dt = {'Tom':90,'Brad':90,'Nick':38,'Brooke':38,'Tucker':200,'Robert':58,'Joe':60,'Joy':120}
def uncommonword(word1,word2):
  count = {}
  b = []
  for i in word1.lower().split():
    # if i not in count:
    #   count[i] = 1
    # else:
    #   count[i] +=1
    count[i] = count.get(i,0)+1

  for i in word2.lower().split():
    # if i not in count:
    #   count[i] = 1
    # else:
    #   count[i] +=1
    count[i] = count.get(i,0) +1

  # for i in count:
  #   if count[i] ==1:
  #     b.append(i)
  # return b
  return [i for i in count if count[i] ==1 ]
