# Write a Program to check whether the number is Neon Number or Not

def sqrt(n):
    i=1
    r=2
    sqrr = 1
    while i <= r:
        sqrr = sqrr * n
        i+=1
    return sqrr    
    # return n**2
    
# print(sqrt(9))
def is_NeonNumber(n):
    orgi = n
    sq = sqrt(n)
    sum = 0
    while sq:
        sum = sum + (sq % 10)
        sq //=10
    if orgi == sum:
        return f'{orgi} is a Neon number'
    return f'{orgi} is not a Neon Number'


print(is_NeonNumber(9))     
