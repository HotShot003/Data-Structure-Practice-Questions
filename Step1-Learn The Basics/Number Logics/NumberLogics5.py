# Write a program to count the number of digits in an integer.

def sum(n):
    s=0
    while n>0:
        s= s + (n%10)
        n=n//10
    return s

print(sum(222))    