# Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.


# Example 1:

# Input:
# N = 5
# arr[] = {4, 1, 3, 9, 7}
# Output:
# 1 3 4 7 9
# Explanation:
# Maintain sorted (in bold) and unsorted subarrays.
# Select 1. Array becomes 1 4 3 9 7.
# Select 3. Array becomes 1 3 4 9 7.
# Select 4. Array becomes 1 3 4 9 7.
# Select 7. Array becomes 1 3 4 7 9.
# Select 9. Array becomes 1 3 4 7 9.
# Example 2:

# Input:
# N = 10
# arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
# Output:
# 1 2 3 4 5 6 7 8 9 10

# Your Task:  
# You dont need to read input or print anything. Complete the functions select() and selectionSort() ,where select() takes arr[] and starting point of unsorted array i as input parameters and returns the selected element for each iteration in selection sort, and selectionSort() takes the array and it's size and sorts the array.


# Expected Time Complexity: O(N2)
# Expected Auxiliary Space: O(1)


# Constraints:
# 1 ≤ N ≤ 10^3


# Ascending :
arr = [4, 1, 3, 9, 7]

def SelectionSort(arr, n):
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the elements
    return arr

print(SelectionSort(arr, len(arr)))


# Descending :

arr = [4, 1, 3, 9, 7]
def SelectionSort1(arr, n):
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the elements
    return arr

print(SelectionSort1(arr, len(arr)))
