"""
Sorted squareed Array
Given a sorted interger array, find square of the given array,
and return the sorted squared array.

input : [-6,-4,1,2,3,5]
output : [1,4,9,16,25,36]
"""

def sortsqar(lst):
    n = len(lst)
    retVal = list(range(n))
    
    left,right = 0,n-1
    ind = n-1
    
    for i in range(n-1,-1,-1) :
        if abs(lst[left]) > abs(lst[right]) :
            retVal[i] = lst[left] * lst[left]
            left += 1
        else :
            retVal[i] = lst[right] * lst[right]
            right -= 1
            
    return retVal
    
    
print ("\nSorted squareed Array : ",sortsqar([-6,-4,1,2,3,5]))
