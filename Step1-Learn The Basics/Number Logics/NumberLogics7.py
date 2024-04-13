# Write a program to calculate G.C.D or HCF of two numbers.

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(gcd(64,96))    
    
# GCD of 64 and 96 is 32.