# Write a program to find out all Perfect numbers present within a
# given range.


def perfectNum1(s,e):
    prfnum=[]
    for j in range(s,e+1):
        n=j
        sum = 0
        for i in range(1, n//2+1):
            if n % i == 0:
                sum += i
        if sum == n:
            prfnum.append(n)
    return prfnum

print(perfectNum1(1,100))   
