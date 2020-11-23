'''
Find Missing And Repeating 
Medium Accuracy: 27.42% Submissions: 6988 Points: 4
Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2, …N} is missing and 
one number 'B' occurs twice in array. Find these two numbers.

Example 1:

Input:
N = 2
Arr[] = {2, 2}
Output: 2 1
Explanation: Repeating number is 2 and 
smallest positive missing number is 1.
Example 2:

Input:
N = 3
Arr[] = {1, 3, 3}
Output: 3 2
Explanation: Repeating number is 3 and 
smallest positive missing number is 2.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
'''

def findRepMisEle(lst):
    n = len(lst)
    for i in range(n):
        if lst[abs(lst[i])-1] > 0:
            lst[abs(lst[i])-1] = -lst[abs(lst[i])-1]
        else :
            print ("\nRepeating Element is : ",abs(lst[i]))
    print ("lst : ",lst)
    for i in range(n):
        if lst[i] > 0 :
            print ("\nMissing Element is : ",(i+1))
    
    
lst = [7, 3, 4, 5, 5, 6, 2]
print ("\n Find Missing And Repeating : ",findRepMisEle(lst))
