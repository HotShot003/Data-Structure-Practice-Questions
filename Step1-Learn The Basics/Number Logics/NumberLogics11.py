# Write a Program to calculate prime Factors of number.Write a Program to calculate prime Factors of number.
# Sol 1:

def PrimeFactor(n):
    list = []
    i=2
    while i <= n//2+1:
        if n%i == 0:
            list.append(i)
            n = n//i
        else:
            i += 1
    list.append(n)
    return list

print(PrimeFactor(20))


# Sol 2:

# def primefact(n):
#     pnlist = []
#     i = 2
#     while i <= n:
#         if n % i == 0 :
#            pnlist.append(i)
#            n = n//i
#         else :
#             i+=1
#     return pnlist               

# print(primefact(12))