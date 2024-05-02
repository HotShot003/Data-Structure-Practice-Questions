# Write a program to find out all Harshad numbers present within a
# given range.


def digitSum(n):
    sum = 0
    while n:
        sum = sum + (n%10)
        n=n//10
    
    return sum

# print(digitSum(19))   
 
def HarshadNumber(s,e):
    hrdnum=[]
    for n in range(s,e+1):    
        orgi = n

        if n%digitSum(n) == 0:
            hrdnum.append(n)
        
    return hrdnum 

print(HarshadNumber(1,18))
