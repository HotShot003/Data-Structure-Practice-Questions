
def Largest2Sum(n):
    
    if len(n) <= 0:
        return []
    maxnum = 0
    for i in n:
        if i >= maxnum:
            maxnum = i
    maxnum-=1       # Reason Bcoz here we have accending order (eg=1,1,2,2,3,3,4,5,6,7,7) input if we find max ele then -1 that we get second hightest ele 
    c = 0
    for k in n :
        if k == maxnum:
            c+=1
    return c

print(Largest2Sum(n=[1,1,2,2,3,4,4,5,5,5,6]))        