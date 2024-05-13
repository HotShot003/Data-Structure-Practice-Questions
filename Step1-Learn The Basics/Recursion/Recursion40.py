# 18. find all indices of a number
# Examples:
# Input:
# arr[N] = {1, 2, 3, 2, 2, 5}
# x = 2
# Output:
# 1 3 4


def find_index(arr,val,index=0,res=[]):
    
    if index == len(arr):
        return res
    
    if arr[index] == val:
        res.append(index)
        
    return  find_index(arr,val,index+1,res)


arr=[2,2,2,2,23,322,23,2,2123,21,2,2]

print(find_index(arr,2))        
    