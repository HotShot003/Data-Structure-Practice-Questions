# Write a program to find out all Automorphic numbers present within
# a given range.
  
def squareN(x):
    
    n=2
    i=1
    sqr=1
    while i <= n:
        sqr = sqr * x
        i = i + 1
    return sqr

# print(squareN(5))

def AutomorphicNumber(s,e):
    atmnum=[]
    for n in range(s,e+1):
        orgi = n%10
        sqrorgi = squareN(n)%10
        
        # print(orgi,sqrorgi)
        
        if orgi == sqrorgi :
            atmnum.append(n)
    return atmnum
print(AutomorphicNumber(1,100))            