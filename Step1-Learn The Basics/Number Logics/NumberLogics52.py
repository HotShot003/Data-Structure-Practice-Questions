# Write a program to find the nth prime number.

def is_PrimeNumber(n):
    
    if (n!=2 and n%2==0) or (n!=3 and n%3==0) or (n!=5  and n%5==0):
        return False
    
    
    i=5
    
    while i*i<n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True

# print(is_PrimeNumber(37))  

def nth_PrimeNumber(n):
    
    count = 0
    curr_num = 1
    
    while count < n :
        if is_PrimeNumber(curr_num):
            count += 1
        if count == n :
            return curr_num    
        curr_num += 1
    return curr_num - 1

print(nth_PrimeNumber())