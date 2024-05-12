# 1. Print Decreasing
# 1. You are given a positive number n.
# 2. You are required to print the counting from n to 1.
# 3. You are required to not use any loops.
# Examples:
# Input : 5
# Output :
# 5
# 4
# 3
# 2
# 1


def prt(n):
    if n == 0:
        return
    print(n)
    prt(n-1)

prt(5)    