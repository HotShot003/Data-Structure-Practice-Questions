# Write a program to find out all perfect square numbers present within
# a given range.


def squareRoot(n):
    i=1
    while i*i <=n:
        if i*i == n:
            return True
        i+=1
    return False
# print(squareRoot(4))    

def range_perfectSqr(s,e):
    persqr = []
    for n in range(s,e+1):
        if squareRoot(n) :
            persqr.append(n)
    
    return persqr

print(range_perfectSqr(1,25))        