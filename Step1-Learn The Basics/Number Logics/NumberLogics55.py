# Write a program to find the nth strong number.


def fact(n):
    f1=1
    f2=1
    
    while n:
        f1=f1*f2
        f2=f2+1
        n=n-1
    return f1

# print(fact(5))    

def numlen(n):
    c=0
    while n:
        n=n//10
        c=c+1
    return c

def is_StrongNumber(n):
    orgi = n
    sum=0
    l = numlen(n)
    i=1
    while i <= l:
        sum = sum + fact(n%10)
        n//=10
        i+=1
    
    return True if  orgi == sum else False

# print(is_StrongNumber(145))

def nth_StrongNumber(n):
    count = 0 
    curr_num = 1
    
    while count < n :
        if is_StrongNumber(curr_num):
            count +=1
            
        if count == n:
            return curr_num
        
        curr_num +=1
        
    return curr_num - 1     


print(nth_StrongNumber(3))   

