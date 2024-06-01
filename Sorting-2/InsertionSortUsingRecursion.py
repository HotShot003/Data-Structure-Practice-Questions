def InsertionSortRec(arr,n):
    
    if n <= 1:
        return arr
    
    InsertionSortRec(arr,n-1)
    
    last = arr[n-1]
    j = n-2
    
    while j>=0 and arr[j] > last:
        arr[j+1] = arr[j]
        j-=1
        
        
    arr[j+1] = last

def pntRes(arr,n):
    InsertionSortRec(arr, n)
    print("Sorted array is:")
    print(arr)

arr = [5,4,3,2,1]
n = len(arr)
pntRes(arr,n)