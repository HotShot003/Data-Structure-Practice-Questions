# Write a program to check whether a given number is prime or not.

def is_prime(num):
    
    if (num!=2 and num%2==0) or (num!=3 and num%3==0) or (num!=5 and num%5==0):
        return f"{num} is Not Prime"
    i=5
    while i*i<num:
        if num%i==0 or num%(i+2)==0:
            return f"{num} is Not Prime"
        i+=6
    return f"{num} is Prime"

print(is_prime(37))