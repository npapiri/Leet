# 4.) Given a dictionary, print the key for nth highest value present in the dict. If there are more than 1 record present for nth highest value then sort the key
# and print the first one (alphabetically). N can be higher than the number of elements in the dictionary.

ct = {'Brooke':200,'Tucker':200,'Joy':120,'Tom':90,'Brad':90,'Joe':60,'Robert':58,'Nick':38,}

def mynth(ct,n):
  a = []

  for i,v in ct.items():
    if ct[i] not in a:
      a.append(ct[i])

  if n >= len(a):
    n = n - len(a)

  a= sorted(a, reverse = True)
  b = sorted([k for k,v in ct.items() if v == a[n]], reverse = False)
  print(b)
