# 3. Print Increasing Decreasing
# 1. You are given a positive number n.
# 2. You are required to print the counting from n to 1 and back to n again
# 3. You are required to not use any loops.
# Examples:
# Input : 5
# Output :
# 5 4 3 2 1
# 1 2 3 4 5


def prt(n):
    if n==0:
        return
    print(n,end=' ')
    prt(n-1)
    print(n,end=' ')

    
prt(5)    