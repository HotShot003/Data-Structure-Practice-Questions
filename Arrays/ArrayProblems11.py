# MAx Concecutive 1's

def findMaxConsecutiveOnes(nums):
        mc = 0
        c=0
        for i in nums:
            if i == 1:
                c+=1
            else :
                mc = max(mc,c)
                c=0    
            
        return max(mc,c)
    

print(findMaxConsecutiveOnes([1,1,1,3,42,1,1,1,1,0,1,1,1,]))    