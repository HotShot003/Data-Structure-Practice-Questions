# Write a program to find the nth Hashed number.

def digitSum(n):
    
    sum = 0 
    while n :
        sum += n % 10
        n = n // 10
    return sum    

def is_HarshadNumber(n):
    
    if n % digitSum(n) == 0:
        return True
    
    return False

def nth_HarshadNumber(n):
    
    count = 0
    
    curr_num = 1
    
    while count <= n:
        if is_HarshadNumber(curr_num):
            count += 1
        if count == n :
            return curr_num
        
        curr_num +=1
    return curr_num - 1

print(nth_HarshadNumber(12))        