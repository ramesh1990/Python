'''
Transpose of a matrix is a task we all can perform very easily in python (Using a nested loop).
But there are some interesting ways to do the same in a single line.
In Python, we can implement a matrix as nested list (list inside a list).
Each element is treated as a row of the matrix. For example m = [[1, 2], [4, 5], [3, 6]] represents
a matrix of 3 rows and 2 columns.
First element of the list – m[0] and element in first row, first column – m[0][0].
'''

def transpose(lst) :
    # Loop Method
    result = []
    for i in range(len(lst[0])):
        tmp = []
        for j in range(len(lst)):
            tmp.append(lst[j][i])
        result.append(tmp)

    # List comprihrnce method
    result = [[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]
    return result

print ("Matrix Transpose : ",transpose([[1,2,3],[4,5,6]]))
