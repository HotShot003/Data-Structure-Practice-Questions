# Logest Subarray with sum 0

# Sol 1:
# Time: O(n^2)
def BruteForce(n,arr):
    maxlen=0
    for i in range(n):
        sum = 0
        for j in range(i+1,n):
            sum += arr[j]
            if sum == 0:
                maxlen = max(maxlen,j-i)
    
    return maxlen



arr=[9, -3, 3, -1, 6, -5]
print(BruteForce(len(arr),arr))            


# Sol 2:

def longsubarr(n,arr):
    # pass
    
    presum = {}
    sum = 0
    maxlen = 0
    
    for i in range(n):
        
        sum += arr[i]
        
        if sum == 0:
            maxlen = max(maxlen,i+1)
        
        rem = sum 
        if rem in presum:
            length = i - presum[rem]
            maxlen = max(maxlen,length)
        
        else:
            presum[rem] = i
    return maxlen        

arr=[9, -3, 3, -1, 6, -5]
print(longsubarr(len(arr),arr))
    