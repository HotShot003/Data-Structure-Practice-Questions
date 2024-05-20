# # Set Matrix Zero

# Problem statement
# You are given a matrix 'MATRIX' of dimension 'N' x 'M'. Your task is to make all the elements of row 'i' and column 'j' equal to 0 if any element in the ith row or jth column of the matrix is 0.

# Note:

# 1) The number of rows should be at least 1.

# 2) The number of columns should be at least 1.

# 3) For example, refer to the below matrix illustration: 

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= N <= 100
# 1 <= M <= 100
# -10^9 <= MATRIX[i][j] <= 10^9

# Where 'MATRIX[i][j]' denotes the matrix element.
# Follow Up:

# Can you solve it with the space complexity of O(1)?

# Time limit: 1 sec


# Sample Input 1:
# 2 3
# 2 4 3
# 1 0 0
# Sample Output 1:
# 2 0 0 
# 0 0 0 
# Sample Input 2:
# 1 1 
# 5
# Sample Output 2:
# 5 


# Hints:
# 1. Think about how to identify the rows and columns containing a '0' element and then modify the matrix accordingly to make all elements in those rows and columns equal to 0.
# 2. You can use the first row and first column of the matrix itself as indicators to mark whether a particular row or column needs to be zeroed


# Sol 1: Brute Force  [O(n^3)]

def rowZero(arr,n,m,i):
    for j in range(m):
        if arr[i][j] != 0:
            arr[i][j] = -1

def colZero(arr,n,m,j):
    for i in range(n):
        if arr[i][j] != 0:
            arr[i][j] = -1

def setZeros(arr,n,m):
   
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                rowZero(arr,n,m,i)
                colZero(arr,m,n,j)
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == -1:
                arr[i][j] = 0
    
    return arr
arr=[[1,1,1],[1,0,1],[1,1,1]]
n = len(arr)
m = len(arr[0])
print(setZeros(arr,n,m))            
            
            
# Sol 2:  time complexity O(n^2) and space O(n)

def setZeros1(arr,n,m):
    row = [0]*n
    col = [0] * m
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                row[i] = 1
                col[j] = 1
    
    for i in range(n):
        for j in range(m):
            
            if row[i] or col[j]:
                
                arr[i][j] = 0            
    
    return arr

arr=[[1,1,1],[1,0,1],[1,1,1]]
print(setZeros1(arr,n,m))            


# Sol 3:  Try to Reduce Space complexity]  Space [O(1)]

def setZeros2(arr,n,m):
    
    col0 = 1
    
    
    for i in range(n):
        for j in range(m):
            
            if arr[i][j] == 0:
                
                arr[i][0] = 0
                
                if j!=0:
                    arr[0][j] = 0
                
                else :
                    col0 = 0
    
    for i in range(n):
        for j in range(m):
            
            if arr[i][j] != 0:
                
                if arr[0][j] == 0 or arr[i][0]==0:
                    arr[i][j] = 0
    
    for j in range(m):
        
        if arr[0][j] == 0:
            arr[i][j] = 0
    
    for i in range(n):
        
        if col0 == 0:
            arr[i][0] = 0   
    return arr

arr=[[1,1,1],[1,0,1],[1,1,1]]

print(setZeros2(arr,n,m))                
         
                        
