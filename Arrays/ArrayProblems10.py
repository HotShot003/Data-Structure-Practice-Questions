# Find Intersection of Two Arrays ::


arr1 = [1,2,3,4,5,6,7]
arr2 = [2,3,5,6,8]
res = []
i=j=0
while i<len(arr1) and j<len(arr2):
    
    if arr1[i] < arr2[j]:
        i+=1
    
    elif arr1[i] > arr2[j]:
        j+=1
    
    elif arr1[i] == arr2[j]:
        res.append(arr1[i])
        i+=1
        j+=1

print(res)        
                 
