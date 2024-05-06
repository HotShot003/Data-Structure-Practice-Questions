# Write a program to find the nth perfect number.

def is_PerfectNumber(n):
    
    sum = 0
    
    for i in range(1,n//2+1):
        if n % i == 0 :
            sum +=i
    return sum 

# print(is_PerfectNumber(28))         

def  nth_PerfectNumber(n):
    count = 0
    curr_num = 1
    
    while count <= n:
        if is_PerfectNumber(curr_num) == curr_num:
            count += 1
        
        if count == n :
            return curr_num
        curr_num += 1
    
    return curr_num - 1

print(nth_PerfectNumber(2))