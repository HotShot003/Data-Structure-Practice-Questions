# Count subarrays with xor with k

# Sol 1: Brute Force

def xorsubarr(arr,k):
    
    n = len(arr)
    c = 0
    
    for i in range(n):
        for j in range(i,n):
            if (arr[i] ^ arr[j]) == k:
                c += 1
    return c
arr=[4, 2, 2, 6, 4]
k=6
print(xorsubarr(arr,k))


# Sol 2 ; Optimal

def xorsubarr1(arr,k):
    
    n = len(arr)
    
    mapp={}
    xr = 0
    mapp[xr]=1
    
    c = 0
    
    for i in range(n):
        
        xr = xr ^ arr[i]
        
        x = xr ^ k
        
        if x in mapp:
            c += mapp[x]
        
        if xr in mapp:
            mapp[xr] += 1
        
        else : mapp[xr] = 1
    
    return c
arr=[4, 2, 2, 6, 4]
k=6
print(xorsubarr1(arr,k))        