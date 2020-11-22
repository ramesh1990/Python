'''
Find Longest subarray by Sum.
input : 
lst = [1,2,3,4,5,0,0,0,6,7,8]
k = 15
output : (0,7)
'''

def LongSubarray (lst,k):
    # Sliding Window Protocl Method 
    left , right = 0,0
    result = [0,0]
    sum = 0
    lenOfsubarray = 0
    
    while ( right < len(lst) ):
        sum += lst[right]
        while ( sum > k and left < right) :
            sum -= lst[left]
            left += 1
        
        if ( sum == k and (result[1] - result[0] < right - left)):
            result[0] = left+1
            result[1] = right+1
            
        right += 1
    return result
    
lst = [1,2,3,4,5,0,0,6,7,8]
k = 15

print ("\n Find Longest subarray by Sum : ",LongSubarray(lst,k))    
