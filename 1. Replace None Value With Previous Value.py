# Replace None value with previous value present in a list.

y =[None, None, 1, 2, None, None, 3, 4, None, 5, None, None]

def replace(y):
  for i,v in enumerate(y[:-1],1):
    if v is None:
      v=y[i-1]
  return y
