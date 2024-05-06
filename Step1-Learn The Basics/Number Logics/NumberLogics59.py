# Write a program to find the nth automorphic number.

def numSquare(n):
    return n * n

# print(numSquare(5))

def is_AutoMorphicNumber(n):
    
    orgi = n % 10
    
    sqr = numSquare(n) % 10
    
    if orgi == sqr :
        return True
    return False

def nth_AutoMorphicNumber(n):
    
    count = 0
    
    curr_num = 1
    
    while count <= n :
        if is_AutoMorphicNumber(curr_num) :
            count += 1
        if count == n :
            return curr_num
        curr_num += 1
    return curr_num - 1

print(nth_AutoMorphicNumber(5))    