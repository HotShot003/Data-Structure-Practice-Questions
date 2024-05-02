# Write a program to find out all Abundant numbers present within a
# given range.


def factorSum(n):
    sum = 0
    i=1
    while i<=n//2:
        if n%i == 0:
            sum += i
        i += 1
    return sum
# print(factorSum(6))

def AbundantNumber(s,e):
    abtnum=[]
    for n in range(s,e+1):
        orgi = n
        if factorSum(n) > orgi:
           abtnum.append(n)
    return abtnum       
           
print(AbundantNumber(1,100))
