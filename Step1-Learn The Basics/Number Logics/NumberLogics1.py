# Write a program to the sum of n natural numbers.

# Sol 1:
def Sum1(n):
    if n<=0:
        print("Enter a Natural Number !")
        return
    sum=0
    x=1
    while x<=n:
        sum=sum+x
        x=x+1
    print(sum) #Or u can rteturn it also

Sum1(5)

# Sol 2:

def Sum2(n):
    if n<=0:
        print("Enter a Natural Number !")
        return
    return (n*(n+1))//2
print(Sum2(3))


#Output :
# 6
# 6