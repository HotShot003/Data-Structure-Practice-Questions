# Write a program to find out all Strong numbers present within a
# given range.


def factorial(n):
    f1=1
    f2=1
    while n:
        f1=f1*f2
        f2+=1
        n-=1
    return f1

# print(factorial(5))    

def numlen(n):
    c=0
    while n:
        n=n//10
        c+=1
    return c

def range_StrongNumber(s,e):
    stg=[]
    for i in range(s,e+1):
        orgi = i
        l=numlen(i)
        sum=0
     
        while i>0:
            sum = sum + factorial(i%10)
            i=i//10

        if sum == orgi:
            stg.append(orgi)
    return stg               
    
print(range_StrongNumber(1,40585))

