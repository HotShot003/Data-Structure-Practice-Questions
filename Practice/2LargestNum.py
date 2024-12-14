
def Largest2Sum(n):
    
    if len(n) <= 0:
        return []
    maxnum = 0
    for i in n:
        if i >= maxnum:
            maxnum = i
    maxnum-=1        
    c = 0
    for k in n :
        if k == maxnum:
            c+=1
    return c

print(Largest2Sum(n=[1,1,2,2,3,4,4,5,5,5,6]))        