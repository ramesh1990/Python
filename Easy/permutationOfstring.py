'''
Permutations of a given string 
Basic Accuracy: 32.48% Submissions: 97910 Points: 1
Given a string S. The task is to print all permutations of a given string.

Input:
The first line of input contains an integer T, denoting the number of test cases. Each test case contains a single string S in capital letter.

Output:
For each test case, print all permutations of a given string S with single space and all permutations should be in lexicographically increasing order.

Constraints:
1 ≤ T ≤ 10
1 ≤ size of string ≤ 5

Example:
Input:
2
ABC
ABSG

Output:
ABC ACB BAC BCA CAB CBA 
ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA

Explanation:
Testcase 1: Given string ABC has permutations in 6 forms as ABC, ACB, BAC, BCA, CAB and CBA .
'''

def to_print(string):
    print (''.join(string))

def permutations(string,left,right):
    if left == right :
        to_print(string)
    else :
        for i in range(left,right+1):
            string[left],string[i] = string[i],string[left]
            permutations(string,left+1,right)
            string[left],string[i] = string[i],string[left]
        
string = 'ABCD'
n = len(string)
a = list(string)

permutations(a,0,n-1)
