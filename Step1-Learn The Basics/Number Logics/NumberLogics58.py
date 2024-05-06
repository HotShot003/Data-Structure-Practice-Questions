# Write a Program to Find nth Abundant Number.

def factorSum(n):
    sum = 0
    i=1
    while i<=n//2:
        if n%i == 0:
            sum += i
        i += 1
    return sum
# print(factorSum(6))

def AbundantNumber(n):
    orgi = n
    if factorSum(n) > orgi:
        return True
    return False

# print(AbundantNumber(12))

def nth_AbundantNumber(n):
    
    count = 0
    curr_num = 1
    
    while count <= n:
        
        if AbundantNumber(curr_num):
            count+=1
        
        if count == n :
            return curr_num
        
        curr_num+=1
    
    return curr_num - 1        


print(nth_AbundantNumber(1))