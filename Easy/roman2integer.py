'''
Roman Number to Integer 
Easy Accuracy: 44.16% Submissions: 1251 Points: 2
Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their values are given below.
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

Example 1:

Input:
s = V
Output: 5
Example 2:

Input:
s = III 
Output: 3
'''

def roman2int(string):
    roman_val = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'L':50,'C':100,'D':500,'M':1000,'XL':40,'XC':90,'CD':400,'CM':900}
    i,num = 0,0
    
    while i < len(string):
        if i+1 < len(string) and str(string[i:i+2]) in roman_val :
            num += roman_val[string[i:i+2]]
            i += 2
        else :
            num += roman_val[string[i]]
            i += 1
    return num
    
s = 'IV'
print ("\n Roman Number to Integer  : ",roman2int(s))
