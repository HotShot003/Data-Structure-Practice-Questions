
# Majority Element [ > n/3]



def MajorityEle(arr):
    n = len(arr)
    res = []
    
    for i in range(n):
        if len(res) == 0 or arr[i] not in res:
            count = arr.count(arr[i])
            if count > (n // 3):
                res.append(arr[i])
                
        if len(res) == 2:
            break    
    return res

arr = [11, 33, 33, 11, 33, 11]
print(MajorityEle(arr))


# Sol 2: Hashing

def Majority1(arr):
    
    dic = dict()
    ans = []
    n = len(arr)
    
    for i in arr:
        
        if i in dic :
            dic[i] += 1
        else:
            dic[i] = 1
    
    for i,count in dic.items():
        if count > n // 3:
            ans.append(i)
            
    return ans

arr = [1, 1, 1, 1, 3, 2, 2, 2]
print(Majority1(arr))