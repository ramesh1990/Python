'''
Reverse words in a given string 
Easy Accuracy: 50.0% Submissions: 22297 Points: 2
Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

Example 1:

Input:
S = i.like.this.program.very.much
Output: much.very.program.this.like.i
Explanation: After reversing the whole
string(not individual words), the input
string becomes
much.very.program.this.like.i
Example 2:

Input:
S = pqr.mno
Output: mno.pqr
Explanation: After reversing the whole
string , the input string becomes
mno.pqr

'''

def revSentence(string):
    return '.'.join(string.split('.')[::-1])
    
s = 'i.like.this.program.very.much'
print ("\n Reverse words in a given string : ",revSentence(s) )
