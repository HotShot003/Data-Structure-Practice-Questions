# Write a Program to Find nth Armstrong Number.

def powerFunc(m,n):
    
    p=1
    while n:
        p*=m
        n-=1
    return p

#To calculate the digits
def lenFunc(n):
    c=0
    while n :
        n//=10
        c+=1
    return c

def is_Armstrong(n):
    original_number=n
    l=lenFunc(n)
    i=1
    sum=0
    while i<=l:
        sum +=powerFunc(n%10,l)
        n//=10
        i+=1
    return True if sum == original_number else False      

# print(Armstrong(153))

def nth_ArmstrongNumber(n):
    
    count = 0
    
    curr_num = 1
    
    while count < n:
        if is_Armstrong(curr_num):
            count += 1
        if count == n:
            return curr_num
        curr_num += 1
        
    return curr_num - 1

print(nth_ArmstrongNumber(10))