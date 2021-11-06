# 5*) Given a list of ints, balance the list so that each int appears equally in the list. Return a dictionary where the key is the int and the value is the count needed to balance the list.

a = [1,1,1,1,2,3,2,21,14]
b = {}
c = {}
for i in a:
  b[i] = b.get(i,0)+1

max_values = max(b.values())

for i in b:
  if b[i] !=max_values:
    c[i] = (max_values-b[i])
  else:
    c[i] = 0
print(c)
