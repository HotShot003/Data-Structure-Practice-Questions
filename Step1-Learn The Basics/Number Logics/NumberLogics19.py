# Write a program to check whether a given number is an Abundant
# number or not.

def factorSum(n):
    sum = 0
    i=1
    while i<=n//2:
        if n%i == 0:
            sum += i
        i += 1
    return sum
# print(factorSum(6))

def AbundantNumber(n):
    orgi = n
    if factorSum(n) > orgi:
        return f'{orgi} is a Abundent Number'
    return f'{orgi} is a Not Abundent Number'

print(AbundantNumber(12))
