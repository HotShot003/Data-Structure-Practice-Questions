# Write a program to check whether a given number is a perfect
# square number or not.


def perfectSq(n):
    
    i=2
    while i*i<=n:
        if i*i==n:
            return True
        i+=1
    return False

print(perfectSq(4))
