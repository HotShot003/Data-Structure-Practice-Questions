# Write a program to find out all Armstrong numbers present within a
# given range.


def numlen(n):
    c = 0
    while n:
       n = n // 10
       c += 1
    return c

def powerFunc(m, n):
    p = 1
    while n:
        p = p * m
        n -= 1
    return p

def range_ArmstrongNum(s, e):
    arm = []
    for n in range(s, e + 1):
        orgi = n
        l = numlen(n)
        sum = 0
        i = 1
        while i <= l:
            sum = sum + powerFunc(n % 10, l)
            n = n // 10
            i += 1
        if sum == orgi:
            arm.append(orgi)
    
    return arm    

print(range_ArmstrongNum(1, 200))


