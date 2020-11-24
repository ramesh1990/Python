'''
Implement Atoi 
Basic Accuracy: 32.9% Submissions: 53493 Points: 1
Your task  is to implement the function atoi. The function takes a string(str) as argument and converts it to an integer and returns it.

Example 1:

Input:
str = 123
Output: 123

Example 2:

Input:
str = 21a
Output: -1
Explanation: Output is -1 as all
characters are not digit only.
'''

def AtoI(string):
    res = 0
    i = 0
    sign = 1
    if string[0] == '-':
        sign = -1
        i = 1
   
    for ch in string[i:]:
        res = res * 10 + (ord(ch)- ord('0'))
    
    return res * sign
    
s = '-123'
print ("\n A to I : ",AtoI(s),type(AtoI(s)))
