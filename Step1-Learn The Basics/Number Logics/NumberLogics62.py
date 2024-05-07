# Write a Program to Find nth Spy Number.


def digitSum(n):
    s=0
    m=1
    while n :
        s=s+n%10
        m=m*(n%10)
        n=n//10
    return s,m


def spy_Number(n):
    orgi = n
    s,m=digitSum(n)
    if s==m:
        return True
    return False

def nth_SpyNumber(n):
    
    count = 0 
    curr_num = 1
    
    while count <= n :
        
        if spy_Number(curr_num):
            count += 1
        if count == n :
            return curr_num
        
        curr_num+=1
    return curr_num - 1

print(nth_SpyNumber(11))    

