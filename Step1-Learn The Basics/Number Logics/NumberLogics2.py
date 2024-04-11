# Write a program to compute 1/n!.

def program(n):
    # for counting the factorial using while loop
    s=1
    x=1
    while x<=n:        
        s=s*x
        x=x+1
    return s 
# print(program(4)) 
def byfact(n):
    #call program func
    ans =  program(n)
    #print the answer
    print(1/ans)  

# Drivers Code:        
byfact(5)        

        