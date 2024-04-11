# Write a program to compute x^n/n!.

def program(n):
    # for counting the factorial using while loop
    s=1
    x=1
    while x<=n:        
        s=s*x
        x=x+1
    return s 

def exp(x,n):
    #find exponential value

    s=1
    i=1
    while i<=n:
       s=s*x
       i+=1
    return s

# print(exp(2,2))

def compute(x,n):
    top =  exp(x,n)
    bot = program(n)
    res = top / bot
    print(res)   

#Drivers Code

compute(2,2)    