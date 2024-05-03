# Write a Program to Find out all Spy numbers present within a given range.

def digit_sum(n):
    sum=0
    mul=1
    
    while n:
        sum=sum+(n%10)
        mul=mul*(n%10)
        n=n//10
    return sum,mul

# print(digit_sum(1124))    


def range_SpyNumber(s,e):
    
    spyn=[]
    
    for n in range(s,e+1):
        orgi = n
        
        s,m=digit_sum(n)
        
        if s == m :
            spyn.append(orgi)
            
    return spyn

print(range_SpyNumber(100,1000))
        
    