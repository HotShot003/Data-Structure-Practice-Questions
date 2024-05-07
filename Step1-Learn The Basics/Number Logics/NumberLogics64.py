# Write a Program to Find nth Sunny Number.

def perfectSq(n):
    i=2
    while i*i<=n:
        if i*i==n:
            return True
        i+=1
    return False

# print(perfectSq(4))

def is_SunnyNumber(n):
    orgi = n
    
    num = perfectSq(n+1)
    # print(num)
    
    if num:
        return True
    return False


# print(is_SunnyNumber(24))

def nth_SunnyNumber(n):
    
    count = 0 
    curr_num = 1
    
    while count <= n:
        
        if is_SunnyNumber(curr_num):
            count += 1
            
        if count == n:
            return curr_num
        
        curr_num +=1
    return curr_num - 1

print(nth_SunnyNumber(4))        