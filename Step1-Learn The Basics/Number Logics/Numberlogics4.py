# Write a program to count the number of digits in an integer.

def count(n):
    c=0
    while n:
        n=n//10
        c=c+1
        
    return c

print(count(234567))