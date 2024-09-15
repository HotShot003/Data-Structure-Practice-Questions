arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

target = 11

def search2D(arr,target):
    
    m = len(arr)
    n = len(arr[0])
    
    l = 0
    r = n * m - 1
    
    while l <= r:
        
        mid = (l+r) // 2
        row = mid // n
        col = mid % n
        
        if arr[row][col] == target:
            return True
        elif arr[row][col] < target:
            l = mid + 1
        else :
            r = mid - 1    
        
    return False

print(search2D(arr,target))
