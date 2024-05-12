# 7. Print Zigzag
# 1. Here are a few sets of inputs and outputs for your reference
# Input1 -> 1
# Output1 -> 1 1 1
# Input2 -> 2
# Output2 -> 2 1 1 1 2 1 1 1 2
# Examples:
# Input : 3
# Output : 3 2 1 1 1 2 1 1 1 2 3 2 1 1 1 2 1 1 1 2 3

def Zigzag(n):
    if n == 0:
        return 
    
    print(n,end=' ')
    Zigzag(n-1)
    print(n,end=' ')
    Zigzag(n-1)
    print(n,end=' ')

Zigzag(2)    