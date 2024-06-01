# Merge Sort

# Sol 1 : Using Recursion

def merge_sort(arr):
    
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    
    lefthalt = merge_sort(arr[:mid])  # 4      (if n = 9)
    righthalf = merge_sort(arr[mid:]) # 5
    
    return merge(lefthalt,righthalf)

def merge(left,right):
    result = []
    i,j = 0,0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else :
            result.append(right[j])
            j+=1
        
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result



arr = [5,6,3,2,4,1]

print(merge_sort(arr))
        