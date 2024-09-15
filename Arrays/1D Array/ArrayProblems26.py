# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


# Sol :

def SpiralMat(arr):
        res = []

        n = len(arr)
        m = len(arr[0])

        left = 0
        top = 0
        right = m - 1
        bot = n - 1

        while (left <= right) and (top <= bot):

            for i in range(left, right + 1):
                res.append(arr[top][i])
            top += 1

            for i in range(top, bot + 1):
                res.append(arr[i][right])
            right -= 1

            if (top <= bot):
                for i in range(right, left - 1, -1):
                    res.append(arr[bot][i])
                bot -= 1
                
            if (left <= right):
                for i in range(bot, top - 1, -1):
                    res.append(arr[i][left])
                left += 1

        return res

arr=[[1,2,3],[4,5,6],[7,8,9]]
print(SpiralMat(arr))    