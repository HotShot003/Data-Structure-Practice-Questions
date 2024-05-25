# 3 Sum

# Sol : 1 (Brute Force) time = O(n^3)

def sum3(arr):
    
    n = len(arr)
    st = set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = [arr[i],arr[j],arr[k]]
                    temp.sort()
                    st.add(tuple(temp))
    
    # ans = [list(i) for i in st]
    ans = list(st)    
    return ans

arr = [-1,0,1,2,-1,-4]
print(sum3(arr))
                
                
# Sol 2: Optimal(Hashing)

def sum31(arr):
    
    st = set()
    
    n = len(arr)
    
    for i in range(n):
        hashset = set()
        
        for j in range(i+1,n):
            
            third = -(arr[i]+arr[j])
            
            if third in hashset:
                temp = [arr[i],arr[j],third]
                temp.sort()
                st.add(tuple(temp))
            hashset.add(arr[j])    
    
    res = list(st)
    return res

arr = [-1,0,1,2,-1,-4]
print(sum31(arr))        



# Sol 3: More Optimal Two pointer

def threeSum(nums):
        
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            j, k = i + 1, n - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return res

arr = [-1,0,1,2,-1,-4]
print(threeSum(arr))


                