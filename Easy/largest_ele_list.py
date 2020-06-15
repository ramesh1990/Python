"""Write a function that returns the largest element in a list."""

def large(lis):
  max = lis[0]
  for i in lis:
    if i > max :
      max = i
  return max

print ("Max ",large([2,3,4,1,5]))
