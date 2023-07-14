import random

#find the integer not repeated in an array
def lonelyinteger(a):
    
    for i in a:
        if a.count(i)==1:
            return i

#Find the difference between the diagonals of a matrix
def diagonalDifference(arr):
    right_diag=left_diag=0
    l=len(arr[0])
    right_diag=sum([arr[i][i] for i in range(l)])
    left_diag=sum([arr[i][l-1-i]for i in range(l)])
    abs_diff=abs(right_diag-left_diag)
    return abs_diff

#count the freq of the numbers in input array
def countingSort(arr):
    #freq_arr=[0]*(max(arr)+1)
    freq_arr=[0]*100
    for i in arr:
        freq_arr[i]+=1

    return freq_arr

def flippingMatrix(matrix):
    l=len(matrix)
    n=l//2
    s = 0
    for i in range(n):
        for j in range(n):
            s += max(matrix[i][j], matrix[i][l-j-1], matrix[l-i-1][j], matrix[l-i-1][l-j-1])

    return s
    
        
a=[1,2,3,4,3,2,1]
print(lonelyinteger(a))

arr=[[11,2,4], [4,5,6], [10,8,-12]]
print(diagonalDifference(arr))

#arr=[1,1,3,2,1]
arr=[random.randint(1,100) for iter in range(100)]
print(countingSort(arr))

mtx=[[112, 42, 83, 119], [56, 125, 56, 49], [15, 78,101, 43], [62,98,114,108]]
print(flippingMatrix(mtx))
