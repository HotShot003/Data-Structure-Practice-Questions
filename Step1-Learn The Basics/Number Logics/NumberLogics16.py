# Write a program to check whether a given number is a strong number or
# not.



def fact(n):
    f1=1
    f2=1
    while n:
        f1=f1*f2
        f2+=1
        n-=1
    return f1

# print(fact(5))

def lenFunc(n):
    c=0
    while n :
        n=n//10
        c+=1
    return c    

def strongNum(n):
    original_number=n
    i=1
    sum=0
    l=lenFunc(n)
    while i<=l:
        sum = sum + fact(n%10)
        n=n//10
        i+=1
    # return sum
    return f"{original_number} is a Strong Number" if sum == original_number else f"{original_number} is not a Strong Number"

print(strongNum(145))    
        
        