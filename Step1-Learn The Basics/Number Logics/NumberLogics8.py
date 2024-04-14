# Write a program to calculate G.C.D or HCF of two numbers.
# Sol :2
def gcd(num1,num2): 
    if num2>num1:
        mn=num1
    else :
        mn=num2
    for i in range(1,mn+1):
        if num1 % i == 0 and num2 % i ==0:
            gcd=i
    return gcd
print(gcd(12,16))           