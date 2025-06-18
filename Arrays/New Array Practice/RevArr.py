# Reverse an array in-place without using extra space.

# Jugad No. 1
Arr = list(map(int,input().split()))
# print(Arr[::-1])


# Two Pointer Approach

def Rev(Arr):

    l = 0
    r = len(Arr) - 1

    while l < r :
        Arr[l] , Arr[r] = Arr[r] , Arr[l]

        l+=1
        r-=1
    return Arr    

print(Rev(Arr))
