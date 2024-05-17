# Find Missing Number From the Array 

def misNum(arr,n):
    
    has=[0] * (n+1)
    
    for i in range(n):
        
        has[arr[i]] = 1
    # print(has)    
   
    for j in range(len(has)):
        
        if has[j] == 0:
            return j
        

arr = [1,2,0,4,5]
print(misNum(arr,len(arr)))

