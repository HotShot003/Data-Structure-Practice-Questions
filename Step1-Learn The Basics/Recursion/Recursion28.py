# 5. Power-linear
# 1. You are given a number x.
# 2. You are given another number n.
# 3. You are required to calculate x raised to the power n.
# Examples:
# Input : 2 5
# Output : 32


def pow(n,r):
    
    if r == 0:
        return 1
    
    return n * pow(n,r-1)
   
print(pow(2,3))
    
    

    
    