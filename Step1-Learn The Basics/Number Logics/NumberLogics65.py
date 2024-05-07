# Write a Program to Find nth Disarium Number.



def numlen(n):
    c=0
    while n:
        n=n//10
        c+=1
    return c


def is_Disarium(n):
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
        return True
    
    return False

def nth_Disarium(n):
    
    count = 0
    curr_num = 1
    
    while count <= n :
        if is_Disarium(curr_num):
            count += 1
        if count == n :
            return curr_num
        curr_num += 1
    return curr_num - 1

print(nth_Disarium(10))    
    