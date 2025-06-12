# Array Manipulation: Partition Array into Even and Odd  

# 1) My approach
n = int(input())
arr = list(map(int, input().split()))

lis1 = []
lis2 = []

for i in arr:
    if i % 2 == 0:
        lis1.append(i)
    else:
        lis2.append(i)

print(lis1 + lis2)
            
# 2) Ai Approach

# def partition_even_odd(arr, n):
#     # Create two temporary arrays for even and odd numbers
#     even = []
#     odd = []
    
#     # Separate even and odd numbers while maintaining relative order
#     for num in arr:
#         if num % 2 == 0:
#             even.append(num)
#         else:
#             odd.append(num)
    
#     # Combine even and odd arrays
#     result = even + odd
    
#     # Update original array
#     for i in range(n):
#         arr[i] = result[i]
    
#     return arr

# # Input handling
# n = int(input())
# arr = list(map(int, input().split()))
# result = partition_even_odd(arr, n)
# print(*result)