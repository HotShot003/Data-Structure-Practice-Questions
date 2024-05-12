# 2. Print Increasing
# 1. You are given a positive number n.
# 2. You are required to print the counting from 1 to n.
# 3. You are required to not use any loops.
# Examples:
# Input : 5
# Output :
# 1
# 2
# 3
# 4
# 5


def prt(n):
    
    if n== 0:
        return
    prt(n-1)
    print(n)

prt(5)    