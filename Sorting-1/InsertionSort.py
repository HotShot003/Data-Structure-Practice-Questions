# The task is to complete the insert() function which is used to implement Insertion Sort.


# Example 1:

# Input:
# N = 5
# arr[] = { 4, 1, 3, 9, 7}
# Output:
# 1 3 4 7 9
# Example 2:

# Input:
# N = 10
# arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
# Output:
# 1 2 3 4 5 6 7 8 9 10

# Your Task: 
# You don't have to read input or print anything. Your task is to complete the function insert() and insertionSort() where insert() takes the array, it's size and an index i and insertionSort() uses insert function to sort the array in ascending order using insertion sort algorithm. 

# Expected Time Complexity: O(N*N).
# Expected Auxiliary Space: O(1).


# Constraints:
# 1 <= N <= 1000
# 1 <= arr[i] <= 1000

# Sol 1:

def InsertionSort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [5, 4, 3, 2, 1]
print(InsertionSort(arr, len(arr)))


# Sol 2:

# Ascending
def insertion_sort(arr, n):
    for i in range(n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr
arr = [5, 4, 3, 2, 1]
print(insertion_sort(arr, len(arr)))


# Descending :
def insertion_sort1(arr,n):
    
    for i in range(n):
        
        j = i 
        
        while j > 0 and arr[j-1] < arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j -= 1
    return arr
arr = [5, 4, 3, 2, 1]
print(insertion_sort1(arr, len(arr)))       