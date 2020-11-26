'''
Missing number in array
Given an array of size N-1 such that it can only contain distinct integers in the range of 1 to N. Find the missing element.

Example 1:

Input:
N = 5
A[] = {1,2,3,5}
Output: 4
Example 2:

Input:
N = 10
A[] = {1,2,3,4,5,6,7,8,10}
Output: 9
Your Task :
Complete the function MissingNumber() that takes array and N as input and returns the value of the missing number.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 106
1 ≤ A[i] ≤ 106
'''

def missingNumber(arr):
    # method 1 
   # return sum(range(1,len(arr)+2)) - sum(arr)
    # method 2 
    l = len(arr)
    return (l+1)*(n+2)//2 - sum(a) 

print ("\n Msissing one Number in the range Array ",missingNumber([1,2,3,5]))
