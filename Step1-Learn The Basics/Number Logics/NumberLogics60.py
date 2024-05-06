# Write a Program to find the nth Magic Number.

def digit_sum(n):
    
    sum = 0 
    
    while n :
        sum += n % 10

        n = n // 10

    return sum


def is_MagicNumber(n):
    
    while n > 9 :
        n = digit_sum(n)

    return n == 1

# print(is_MagicNumber(55))

def nth_MagicNumber(n):
    
    count = 0 
    
    curr_num  = 1
    
    while count <= n:
        
        if is_MagicNumber(curr_num):
            count += 1
        if count == n :
            return curr_num
        curr_num += 1
    return curr_num - 1


print(nth_MagicNumber(7))