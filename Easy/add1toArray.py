'''
Adding one to number represented as array of digits
Given a non-negative number represented as an array of digits, add 1 to the number(increment the number represented by the digits ). 
The digits are stored such that the most significant digit is first element of array.

Examples :

Input : [1, 2, 4]
Output : [1, 2, 5]

Input : [9, 9, 9]
Output : [1, 0, 0, 0] 

'''

def addOne(lst):
    n = len(lst)
    retVal = [0]*n
    carry = 1
    for i in range(n-1,-1,-1):
        retVal[i] = ( lst[i] + carry ) % 10
        if lst[i] + carry == 10:
            carry = 1
        else :
            carry = 0
    if carry == 1 :
        retVal = [1]+retVal
    return retVal
        
lst = [9,9,9,9]
print ("\n Adding one to number represented as array of digits : ",addOne(lst))
