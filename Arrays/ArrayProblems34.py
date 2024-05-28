# Merge Intervals :


# Sol 1:

def Merge(arr):
    n = len(arr)
    arr.sort()
    ans = []
    
    for i in range(n):
        
        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])
        
        else :
            ans[-1][1] = max(ans[-1][1],arr[i][1])
        
    return ans

arr = [[1,3],[2,4],[5,6]]
print(Merge(arr))             



# Sol 2 :

def Merge1(arr):
    
    arr.sort()
    res = [arr[0]]
    
    for i in arr[1:]:
        if i[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1],i[1])
        else:
            res.append(i)
            
    return res
arr = [[1,3],[2,4],[5,6]]
print(Merge1(arr))        
    