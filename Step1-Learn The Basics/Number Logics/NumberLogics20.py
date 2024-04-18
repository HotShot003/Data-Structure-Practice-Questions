# Write a program to check whether a given number is an
# Automorphic number or not.
   
def squareN(x):
    
    n=2
    i=1
    sqr=1
    while i <= n:
        sqr = sqr * x
        i = i + 1
    return sqr

# print(squareN(5))

def AutomorphicNumber(n):
    
    orgi = n%10
    sqrorgi = squareN(n)%10
    
    # print(orgi,sqrorgi)
    
    if orgi == sqrorgi :
        return f'{n} is the Automorphic Number'

    return f'{n} is not a Automorphic number'

print(AutomorphicNumber(5))            