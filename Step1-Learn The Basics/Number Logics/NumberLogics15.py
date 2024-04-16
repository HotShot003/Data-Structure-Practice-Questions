# Write a program to check whether a given number is an
# Armstrong number or not.

# to calculate Power
def powerFunc(m,n):
    
    p=1
    while n:
        p=p*m
        n=n-1
    return p

#To calculate the digits
def lenFunc(n):
    c=0
    while n :
        n=n//10
        c=c+1
    return c

def Armstrong(n):
    original_number=n
    l=lenFunc(n)
    i=1
    sum=0
    while i<=l:
        sum = sum + powerFunc(n%10,l)
        n=n//10
        i+=1
    return f"{original_number} is Armstrong Number " if sum == original_number else f"{original_number} is not Armstrong Number"        

print(Armstrong(153))