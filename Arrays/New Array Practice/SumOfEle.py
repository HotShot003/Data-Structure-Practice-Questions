# Write a Python function to find the sum of all elements in an array.
# E.g. : 
# I/N = 1 2 3 4 5
# O/P = 15
def Sumarr(arr):
    res = 0
    for i in arr:
        res += i

    return res

arr = list(map(int,input().split()))

print(Sumarr(arr))