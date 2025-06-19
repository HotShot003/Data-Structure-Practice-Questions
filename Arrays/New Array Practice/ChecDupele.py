# Check if an array contains duplicate elements.


def Dup(Arr):

    seen = set()

    for i in Arr:
        if i in seen:
            return True
        seen.add(i)
    return False    


Arr = list(map(int,input().split()))
print(Dup(Arr))