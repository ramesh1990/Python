'''
Find Sum of two number as K.
input : 
A = [0,0,-5,30212]
B = [-10,40,-3,9]
K = -8

output = True, (-5,-3)
'''

def sumOfTwo(lst1,lst2,k):
    hash = {}
    for i in lst1:
        r = k - i
        if i not in hash:
            hash[r] = i
    
    for j in lst2:
        if j in hash:
            return (True,(j,hash[j]))
    
    return -1
    
A = [0,0,-5,30212]
B = [-10,40,-3,9]
K = -8
print ("\nFind Sum of two number as K : ",sumOfTwo(A,B,K))
