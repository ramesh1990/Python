'''
Find First Non Repeating charecter in the given string.
input : 'aaabcccdeed'
outout : b
'''

from collections import OrderedDict

def nonRepeating(string):
    hash = OrderedDict()
    
    for i in string:
        if i not in hash :
            hash[i] = 1
        else :
            hash[i] += 1
    for key in hash:
        if hash[key] == 1:
            return key
    return '-'
    
s = 'aaabcccdeed'
print ("\nFirst Non Repeating charecter : ",nonRepeating(s))
