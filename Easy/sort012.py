'''
Given an array of size N containing 0s, 1s, and 2s; sort the array in ascending order.

Input:
First line of input contains number of testcases T. For each testcase, there will be two lines,
first of which will contain N. The second lines contains the elements of the array.

Output:
Print sorted array.

Your Task:
Complete the function sort012() that takes array and n and sorts the array in place.

Constraints:
1 <= T <= 50
1 <= N <= 10^5
0 <= A[i] <= 2

Example:
Input :
2
5
0 2 1 2 0
3
0 1 0

Output:
0 0 1 2 2
0 0 1
'''

def sort012(lst,n):
    lo = 0
    hi = n-1
    mi = 0
    while ( mi <= hi ):

        if (lst[mi] == 0 ):
            lst[lo],lst[mi] = lst[mi],lst[lo]
            lo += 1
            mi += 1
        elif ( lst[mi] == 1 ):
            mi += 1
        else :
            lst[hi],lst[mi] = lst[mi],lst[hi]
            hi -= 1
    return lst

print (" Sort 0,1,2 : ",sort012([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1],12))
