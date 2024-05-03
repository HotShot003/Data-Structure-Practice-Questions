#Problem 1:

# Write a Program to Find out all the Disarium numbers present within a
# given range.

# def numlen(n):
#     c=0
#     while n:
#         n=n//10
#         c+=1
#     return c


# def is_Disarium(n):
#     orgi = n
#     l=numlen(n)
#     s=0
#     temp = n
#     while temp > 0:
#         digit = temp%10
#         s = s + (digit ** l)
#         temp=temp//10
#         l-=1
#     # return orgi == s
    
#     if s == orgi:
#         return f'{orgi} is a Disarium Num'
    
#     return f'{orgi} is a Not Disarium Num'
    

# print(is_Disarium(22))    



# Problem 2:

# # Write a Program to check whether the number is Disarium Number or Not.
def numlen(n):
    c=0
    while n:
        n=n//10
        c+=1
    return c


def is_Disarium(s,e):
    
    disnum=[]
    
    for n in range(s,e+1):
        
        orgi = n
        l=numlen(n)
        s=0
        temp = n
        while temp > 0:
            digit = temp%10
            s = s + (digit ** l)
            temp=temp//10
            l-=1
        # return orgi == s
        
        if s == orgi:
            disnum.append(orgi)
        
    return disnum
            

print(is_Disarium(1,100))    