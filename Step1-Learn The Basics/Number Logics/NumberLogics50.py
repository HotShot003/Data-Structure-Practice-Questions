# Write a Python program to find the all Catalan numbers between 1 and 1000.

#  Cn = (2n)! // (n+1)! + n!


def fact(n):
    
    sum = 1
    
    while n>0:
        
        sum=sum * n
        n-=1
    return sum

# print((fact(4+1) * fact(4)))   


def Catalan(val):
    
    orgi = val
    
    Cn= fact(2*val) // (fact(val+1) * fact(val)) 
       
    return Cn

print(Catalan(4)) 