'''
Minimum Platforms 
Medium Accuracy: 44.94% Submissions: 9950 Points: 4
Given arrival and departure times of all trains that reach a railway station. Your task is to find the minimum number of platforms required for the railway station so that no train waits.
Note: Consider that all the trains arrive on the same day and leave on the same day. Also, arrival and departure times will not be same for a train, but we can have arrival time of one train equal to departure of the other.
In such cases, we need different platforms, i.e at any given instance of time, same platform can not be used for both departure of a train and arrival of another.

Example 1:

Input: N = 6 
arr[] = [900  940 950  1100 1500 1800]
dep[] = [910 1200 1120 1130 1900 2000]
Output: 3
Explanation: 
Minimum 3 platforms are required to 
safely arrive and depart all trains.
Example 2:

Input: N = 3
arr[] = [900 1100 1235]
dep[] = [1000 1200 1240] 
Output: 1
Explanation: Only 1 platform is required to 
safely manage the arrival and departure 
of all trains. 
'''


def minPlatforms(arr,dep,n):
    platforms = []
    
    for i in range(n):
        if len(platforms) == 0 :
            platforms.append(dep[i])
        else :
            flag = 1
            for ind,pre_dep in enumerate(platforms):
                if pre_dep < arr[i] :
                    platforms[ind] = dep[i]
                    flag = 0
                    break
            if flag == 1:
                platforms.append(dep[i])
                
    return len(platforms)
    
#arr = [900,  940, 950,  1100, 1500, 1800]
#dep = [910, 1200, 1120, 1130, 1900, 2000]

arr = [900, 1100, 1235]
dep = [1000, 1200, 1240]

print ("\n Minimum Platforms ReQuired : ",minPlatforms(arr,dep,3))

