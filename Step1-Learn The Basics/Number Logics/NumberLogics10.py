# Write a program to find the factorial of a number

def fact(n):
    s=1
    x=1
    
    while x<=n:
        s=s*x
        x=x+1
    return s

print(fact(5))