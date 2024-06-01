def  BubbleSortRec(arr,n):
    if n==1:
        return
    
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    
    BubbleSortRec(arr,n-1)       
    
def pntRes(arr,n):
    BubbleSortRec(arr, n)
    print("Sorted array is:")
    print(arr)
    
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
pntRes(arr,n)     