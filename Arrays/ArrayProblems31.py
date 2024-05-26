# 4 Sum Problem


# Sol 1: Brute Force
#O(N^4))

def sum4(arr,targer):
    
    n = len(arr)
    
    st = set()
    
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    
                    sum = arr[i] + arr[j]+ arr[k] + arr[l]
                    
                    
                    if sum == targer:
                        temp = [arr[i],arr[j],arr[k],arr[l]]
                        temp.sort()
                        st.add(tuple(temp))
    
    res = list(st)
    
    return res

arr = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
k = 9
print(sum4(arr,k))                    


# Sol 2:  using hashset O(n^3)

def sum41(arr,targer):
    
    n = len(arr)
    
    st = set()
    
    for i in range(n):
        for j in range(i+1,n):
            hashset = set()
            for k in range(j+1,n):
                sum = arr[i]+arr[j]+arr[k]
                fourth = target - sum
                
                if fourth in hashset:
                    temp = [arr[i],arr[j],arr[k],fourth]
                    temp.sort()
                    st.add(tuple(temp))
                hashset.add(arr[k])
    
    res = list(st)
    return res                

nums = [2, 2, 2, 2, 1, 3]
target = 8
print(sum41(nums,target))




class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = set()
        pair_sums = {}

        for i in range(n):
            for j in range(i + 1, n):
                current_sum = nums[i] + nums[j]
                needed = target - current_sum

                if needed in pair_sums:
                    for pair in pair_sums[needed]:
                        if pair[1] < i:
                            quad = (nums[pair[0]], nums[pair[1]], nums[i], nums[j])
                            res.add(quad)

            for k in range(i):
                pair_sum = nums[k] + nums[i]
                if pair_sum not in pair_sums:
                    pair_sums[pair_sum] = []
                pair_sums[pair_sum].append((k, i))

        res = [list(quad) for quad in res]
        return res

# Example usage:
solution = Solution()
arr = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
k = 9
print(solution.fourSum(arr, k))



def fourSum(arr,target):
        n = len(arr)

        ans = []
        arr.sort()

        for i in range(n):
            if i>0 and arr[i] == arr[i-1]:
                continue
            for j in range(i+1,n):
                if j>i and arr[j] == arr[j-1]:
                    continue    

                k = j+1
                l = n-1

                while k < l:

                    sum = arr[i] + arr[j] + arr[k] + arr[l]

                    if sum == target:
                        t = [arr[i],arr[j],arr[k],arr[l]]
                        t.sort()
                        ans.append(t)

                        k+=1
                        l-=1

                        while k<l and arr[k] == arr[k-1]:
                            k+=1

                        while k < l and  arr[l] == arr[l+1]:
                            l-=1

                    elif sum < target:
                        k+=1

                    else :
                        l-=1

        return [len(ans)]      

arr = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
k = 9
print(fourSum(arr, k))


