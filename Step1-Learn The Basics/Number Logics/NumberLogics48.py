# Write a Program to Find out all Evil numbers present within a given range.

def binary(n):
    i=0
    list = []
    
    while n:
        if n%2 == 0:
            list.append(0)
        else:
            list.append(1)
        n = n//2
        i+=1
    list.reverse()
    return list



def is_EvilNumber(s,e):
    
    evil=[]
    
    for num in range(s,e+1):
    
        orgi = num
        l = binary(num)
        c=0
        for i in l :
            if i == 1:
                c+=1
        
        if c%2 == 0:
            evil.append(orgi)
    return evil

print(is_EvilNumber(1,100))       
            