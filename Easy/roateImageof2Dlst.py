'''
Rotate Image of 2D List

Given a square matrix, turn it by 90 degrees in clockwise direction without using any extra space.

Examples :

Input:
Matrix:
 1  2  3
 4  5  6
 7  8  9
Output:
 7  4  1 
 8  5  2 
 9  6  3 
The given matrix is rotated by 90 degree 
in anti-clockwise direction.
'''

def printlst(lst):
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            print (lst[i][j],end= ' ')
        print ("\n")

def roateImage(lst):
    row = len(lst)
    col = len(lst[0])
    if row != col :
        return -1
    
    #Step 1 Transpose the matrix
    print (" Before Transpose : ")
    printlst(lst)
    for i in range(row):
        for j in range(i,col):
            tmp = lst[i][j]
            lst[i][j] = lst[j][i]
            lst[j][i] = tmp
    print (" After Transpose : ")
    printlst(lst)
    for i in range(row):
        for j in range(col//2):
            tmp = lst[i][j]
            lst[i][j] = lst[i][col-1-j]
            lst[i][col-1-j] = tmp
            
    print (" After Rotate Image of the 2D List : ")
    printlst(lst)
    
l = [[1,2,3],[4,5,6],[7,8,9]]
roateImage(l)
