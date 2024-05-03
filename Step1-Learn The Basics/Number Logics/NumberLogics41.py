# Write a Program to Find out all Neon numbers present within a given
# range.


def squaren(n):
    # return n*n
    i=1
    r=2
    mul=1
    while i<=r:
        mul=mul*n
        i+=1
    return mul

# print(squaren(9))  

def range_NeonNum(s,e):
    neonum=[]
    
    for n in range(s,e+1):
        orgi = n
        sq=squaren(n)
        sum=0
        while sq :
            sum = sum +(sq%10)
            sq //=10
        if orgi == sum:
            neonum.append(orgi)
    return neonum        

print(range_NeonNum(1,100))  



            