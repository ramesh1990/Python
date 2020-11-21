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
    
    i,j = 0,n-1
    ind = n-1
    
    while i <= j :
        if abs(lst[i]) > abs(lst[j]) :
            s = lst[i] * lst[i]
            retVal[ind] = s
            print (s)
            i += 1
        else :
            s = lst[j] * lst[j]
            print (s)
            retVal[ind] = s
            j -= 1
        ind -= 1
    return retVal
    
    
print ("\nSorted squareed Array : ",sortsqar([-6,-4,1,2,3,5]))
