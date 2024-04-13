# Write a program to reverse a given number.


def reverseNum(n):
    flag = False
    res = 0
    if n<0:
        flag = True
        n=-n
    while n:
        res = (res * 10 ) + (n%10)
        n=n//10
    return res if not flag else -res

print(reverseNum(-321))        