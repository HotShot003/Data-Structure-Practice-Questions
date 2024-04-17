# Write a program to check whether a given number is a perfect number
# or not.

# SOl 1:

# def perfectNum1(n):
#     sum = 0
#     for i in range(1, n):
#         if n % i == 0:
#             sum += i
#     return f"{n} is a Perfect Number" if n==sum else f"{n} is not a Perfect Number"        
# print(perfectNum1(6))


#Sol 2:

def perfectNum2(n):
    c=0
    l=[0]*(n//2+1)
    l[c-1]=1
    mul=1
    sum=0
    i=1
    while i<=n//2:
        if n%i==0:
            l[i]=i
            sum+=i
            mul = mul * i
            c+=1
        i+=1
    # it returns the sum of divisor ,print divisors , multiplication of divisor ,count of divisor     
    return sum , l , mul , c

print(perfectNum2(6))    