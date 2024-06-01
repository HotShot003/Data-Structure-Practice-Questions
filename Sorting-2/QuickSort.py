
# Pivot is Low
def partition(arr,low,high):
    pivot = arr[low]
    i = low + 1
    
    for j in range(low+1,high+1):
        if arr[j] <= pivot:
            arr[j],arr[i] = arr[i],arr[j]
            i+=1
    arr[low],arr[i-1] = arr[i-1],arr[low]
    return i-1
        
def quickSort(arr,low,high):
    
    if low < high :
        pi = partition(arr,low,high)
        
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
    

# Example usage:
arr = [5,4,3,2,1]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:", arr)


# Pivot is Mid:

def partition1(arr,low,high):
    pivot = arr[(low+high)//2]
    i = low - 1
    j = high + 1
    
    while True:
        i+=1
        while arr[i] < pivot:
            i+=1
        
        j-=1
        while arr[j] > pivot:
            j-=1
        
        if i>j:
            return j 
        
        arr[i],arr[j]=arr[j],arr[i]        
    
def quickSort1(arr,low,high):
    
    if low < high :
        pi = partition(arr,low,high)
        
        quickSort1(arr,low,pi-1)
        quickSort1(arr,pi+1,high)
    

# Example usage:
arr = [43,55,4,22,77,89,7,900]
n = len(arr)
quickSort1(arr, 0, n - 1)
print("Sorted array is:", arr)

   