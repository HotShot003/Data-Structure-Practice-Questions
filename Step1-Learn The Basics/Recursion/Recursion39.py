# 17. Search a Value in Array recursively
# Examples:
# Input:
# arr[N] = {23, 12, 4, 65, 67}
# value = 4
# Output:
# Yes at index 2

def SearchVal(arr,value,index=0):
    
    if index == len(arr):
        return -1
    
    if arr[index] == value:
        return index
    
    return  SearchVal(arr,value,index+1)


arr=[1,2,3,4,5]
print(SearchVal(arr,12))