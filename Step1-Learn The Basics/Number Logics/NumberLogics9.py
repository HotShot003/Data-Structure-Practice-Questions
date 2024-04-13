# Write a program to calculate the LCM of two numbers

def LCM(num1,num2):
    mxnum=max(num1,num2)
    while True:
        if mxnum%num1==0 and mxnum%num2==0:    
            lcm=mxnum
            break
        mxnum +=1 
    return lcm
print(LCM(12,16))    
    