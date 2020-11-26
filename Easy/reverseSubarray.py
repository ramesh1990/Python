'''
Reverse array in groups
Basic Accuracy: 51.16% Submissions: 18779 Points: 1
Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.



Example 1:

Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First group consists of elements
1, 2, 3. Second group consists of 4,5.


Example 2:

Input:
N = 4, K = 3
arr[] = {5,6,8,9}
Output: 8 6 5 9
'''

def reverseSubarray(lst,k):
    start = 0
    result = []
    while start < len(lst):
        if len(lst[start:]) < k :
            result = result + list(reversed(lst[start:]))
            break
        result = result + list(reversed(lst[start:start+k]))
        start += k
    return result

print (" Reverse array in groups : ",reverseSubarray([1,2,3,4,5],3))