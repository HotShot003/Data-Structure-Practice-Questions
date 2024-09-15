# merge two sorted array


# Sol 1:

def merge(a1,a2,n,m):
    
    arr = [0] * (m+n)
    
    l=0
    r=0
    index=0
    
    while l<n and r<m:
        
        if a1[l] <= a2[r]:
            arr[index] = a1[l]
            l+=1
            index+=1
        else :
            arr[index] = a2[r] 
            r+=1
            index+=1
        
    while l < n:
        arr[index] = a1[l]
        l+=1
        index+=1
    
    while r < m:
        arr[index] = a2[r] 
        r+=1
        index+=1
        
    for i in range(n+m):
        if i < n:
            a1[i] = arr[i]     
        
        else :
            a2[i-n] = arr[i]
    arr.sort()
    return arr

a1=[1,7,3]
a2=[4,5,6]
print(merge(a1,a2,len(a1),len(a2)))            


# Sol 2:

def merge1(arr1,arr2,n,m):
    
    l = n -1 
    r = 0
    
    while l >=0 and r < m :
        if arr1[l] > arr2[r]:
            arr1[l],arr2[r]=arr2[r],arr1[l]
        
        else :
            break
    
    for i in range(m):
        arr1.append(arr2[i])
    arr1.sort()
    return arr1
            
a1=[1,7,3]
a2=[4,5,6]
print(merge1(a1,a2,len(a1),len(a2)))            
            