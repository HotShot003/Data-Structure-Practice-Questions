# Write a Program to calculate prime Factors of number.Write a Program to calculate prime Factors of number.

def primefact(n):
    pnlist = []
    i = 2
    while i <= n:
        if n % i == 0 :
           pnlist.append(i)
           n = n/i
        else :
            i+=1
    return pnlist               

print(primefact(630))