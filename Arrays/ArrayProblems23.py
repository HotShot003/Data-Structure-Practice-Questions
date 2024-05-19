# # Longest Concecutive Subsequence :
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# # Sol 1 :  BruteFOrce

def LS(a,s):
    
    for i in range(len(a)):
        if a[i] == s:
            return True
    return False    

def LongCSeq(arr):
    
    n = len(arr)
    longe = 1
    # arr.sort()
    # print(arr)
    for i in range(n):
        
        x = arr[i]
        c = 1
        
        while LS(arr,x+1):
            c += 1
            x += 1
        
        longe = max(longe,c)
    return longe


arr = [111,117,112,114,113,115,116]
# print(LongCSeq(arr))        


# Sol 2: Better O(n)

def LongCSeq1(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    arr.sort()
    last = float('-inf')
    longe = 1
    c = 0
    
    for i in range(n):
        
        if arr[i] - 1 == last:
            c+=1
            last = arr[i]
        
        elif arr[i] != last:
            c=1
            last = arr[i]
        
        longe = max(longe,c)
    return longe         

print(LongCSeq1(arr))   
    

# Sol 3 : Optimal Soln:


def LongCSeq2(arr):
    
    n = len(arr)
    
    if n == 0:
        return 0
    longe = 1
    st = set()
    for _ in range(n):
        st.add(arr[_])
    
    for i in st:
        
        if i - 1 not in st:
            
            c = 1
            x = i
            
            while x+1 in st:
                x+=1
                c+=1
            longe = max(longe,c)    
    return longe
print(LongCSeq2(arr))            
            
             
        
    
    