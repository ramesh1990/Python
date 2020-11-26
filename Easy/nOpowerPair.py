'''
Number of pairs
Medium Accuracy: 30.51% Submissions: 4645 Points: 4
Given two arrays X and Y of positive integers, find the number of pairs such that
xy > yx (raised to power of) where x is an element from X and y is an element from Y.

Example 1:

Input:
M = 3, X[] = [2 1 6]
N = 2, Y[] = [1 5]
Output: 3
Explanation:
The pairs which follow xy > yx are
as such: 21 > 12,  25 > 52 and 61 > 16 .
Example 2:

Input:
M = 4, X[] = [2 3 4 5]
N = 3, Y[] = [1 2 3]
Output: 5
Explanation:
The pairs for the given input are
21 > 12 , 31 > 13 , 32 > 23 , 41 > 14 ,
51 > 15 .
'''

def powerPair(a1,a2,n,m):
    count = 0
    for i in range(n):
        for j in range(m):
            if ( a1[j] == a2[j] ) : continue
            if ( a1[i]**a2[j] > a2[j]**a1[i] ):
                count += 1
    return count

print ("Number of pairs : ",powerPair([2,3,4,5],[1,2,3],4,3))