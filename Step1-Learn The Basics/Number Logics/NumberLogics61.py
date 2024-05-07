# Write a Program to Find nth Neon Number.


def sqrt(n):
    i=1
    r=2
    sqrr = 1
    while i <= r:
        sqrr = sqrr * n
        i+=1
    return sqrr    
    
def is_NeonNumber(n):
    orgi = n
    sq = sqrt(n)
    sum = 0
    while sq:
        sum = sum + (sq % 10)
        sq //=10
    if orgi == sum:
        return True
    return False

def nth_NeonNumber(n):
    
    count = 0
    curr_num = 1
    
    while count <= n:
        if is_NeonNumber(curr_num):
            count += 1
        if count == n :
            return curr_num
        curr_num += 1
    return curr_num - 1

print(nth_NeonNumber(3))    