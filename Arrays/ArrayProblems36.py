# Find Missing Number and Repeating :

# Sol 1: Hashing :

def FindMissingandRepeating(arr):
    n = len(arr)
    
    hash = [0] * (n+1)
    
    for _ in range(n):
        hash[arr[_]] += 1
    
    rep , mis = -1 , -1
    
    for i in range(1,n+1):
        
        if hash[i] == 2:
            rep = i
        elif hash[i] == 0:
            mis = i
        
        if mis != -1 and rep != -1:
            break
    return [rep , mis ]

arr = [3, 1, 2, 5, 4, 6, 7, 5]
print(FindMissingandRepeating(arr))            

