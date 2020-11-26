'''
Find a first duplicate in the given array

input : [2,1,3,5,3,2]
output : 3

'''

def duplicate(lst):
    n = len(lst)
    hash = dict()
    
    for i in lst:
        if i not in hash :
            hash[i] = 0
        else :
            return i
    return -1
    
print ("\n First duplicate in the List : ",duplicate([2,2,3,5,3,2]))
