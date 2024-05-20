# # Rotation of 2D Matrix 90 deg
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

def rot90(arr,n,m):
    
    res= [[0 for _ in range(m)] for _ in range(n)]
    # matrix = []
    # for i in range(rows):
    #     row = []
    #     for j in range(cols):
    #         row.append(0)
    #     matrix.append(row)

    
    for i in range(n):
        for j in range(m):
            
            res[j][n-1-i] = arr[i][j]
    
    return res

arr = [[1,2,3],[4,5,6],[7,8,9]]
n  = len(arr)
m = len(arr[0])

print(rot90(arr,n,m))       


# Sol 2 :

def rot901(arr):
    
    n=len(arr)
    
    for i in range(n):
        for j in range(i):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
    
    for i in range(n):
        arr[i].reverse()
    return arr
arr = [[1,2,3],[4,5,6],[7,8,9]]

print(rot901(arr))            