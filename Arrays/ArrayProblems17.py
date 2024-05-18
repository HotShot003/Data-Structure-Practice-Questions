# Getting All possible sub arrays :
#O(n^2)
def SubArray(arr):
    
    n = len(arr)
    result = []
    
    for i in range(n):
        for j in range(i+1, n+1):
            result.append(arr[i:j])
    
    return result


arr=[1,2,3,4,5]
# print(SubArray(arr))         # Printing All Possible Sub arrays

# Optimise Sol for all posible Sub Arrays

def ProcessSubArrays(arr):
    n = len(arr)
    
    for i in range(n):
        subarray = []
        for j in range(i, n):
            subarray.append(arr[j])
            # Process the current subarray, e.g., print it or calculate its sum
            print(subarray)

# Test the function with a large array
arr1 = [1, 2, 3, 4, 5]
ProcessSubArrays(arr1)


# Sum Of All Subarryas:

def SumSubArrays(arr):
    n = len(arr)
    total_sum = 0
    list1 = []
    for i in range(n):
        subarray_sum = 0
        for j in range(i, n):
            subarray_sum += arr[j]
            list1.append(subarray_sum)
            total_sum += subarray_sum
    
    return total_sum,list1    

print(SumSubArrays(arr))  # Get Total of all Subarrys and [sum of subarrays] 



