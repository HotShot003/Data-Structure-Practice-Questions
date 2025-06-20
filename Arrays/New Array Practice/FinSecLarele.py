# Find the second largest element in an array.


Arr = list(map(int,input().split()))

# Arr.sort()
# print(Arr[-2])


def SecMax(Arr):

    f = float('-inf')
    s = float('-inf')
    
    for i in Arr:

        if i > f:
            s = f
            f = i
        elif f > i > s:
            s = i
    return s

print(SecMax(Arr))            