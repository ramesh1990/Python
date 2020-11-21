"""
Find two integers in the list that mutiplication value as K.
input : [2,4,1,6,5,40,-1]
output : (4,5)
"""

def findmul(lst,k):
    n = len(lst)
    '''
    # Method 1 
    for i in range(n):
        for j in range(i+1,n):
            if lst[i] * lst[j] == k :
                return (lst[i],lst[j])
    ''' 
    # Method 2
    tmp = []
    for i in range(n):
        tmp.append(lst[i])
        for j in range(len(tmp)):
            if lst[i] * lst[j] == k:
                return (lst[i],lst[j])
    return -1
    
k = 20
lst = [2,4,1,6,5,40,-1]
print (f"\n Multiplication of {findmul(lst,k)} in the list as {k}")
