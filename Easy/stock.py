'''
Stock Buy Sell to Maximize Profit
The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days. 
For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by buying on day 0, selling on day 3. 
Again buy on day 4 and sell on day 6. If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.
'''

def stock(lst):
    if ( len(lst) < 2) :
        return 0
    
    min_val = lst[0]
    min_ind = 0
    for i in range(len(lst)):
        if ( lst[i] < min_val ) :
            min_val = lst[i]
            min_ind = i
    max_val = lst[min_ind]
    for j in range(min_ind+1,len(lst)):
        if ( lst[j] > max_val ):
            max_val = lst[j]
         
    return max_val - min_val
    
print (" Stock : ",stock([5,2,6,1,7,8,10,3]))
    
    
