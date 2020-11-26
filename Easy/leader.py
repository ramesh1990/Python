'''
Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader.



Example 1:

Input:
N = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17
as it is greater than all the elements
to its right.  Similarly, the next
leader is 5. The right most element
is always a leader so it is also
included.


Example 2:

Input:
N = 5
A[] = {1,2,3,4,0}
Output: 4 0
'''

def leader(lst):
    lead = []
    for i in range(len(lst)):
        if ( lst[i] > max(lst[i+1:],default=0) ):
            lead.append(lst[i])
    return lead

print ("Leader : ",leader([16,17,4,3,5,2]))