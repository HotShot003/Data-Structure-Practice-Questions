# Move all Zeros to the end of the arrray and Return it


# Sol 1: (It always return sorted array for non-zeros elements so it may be problem)

def moveZeros(arr):
    count = 0
    for i in range(len(arr)):
        
        if arr[i] == 0:
            count +=1
    arr.sort()
    k=count
    arr[:] = arr[k:] + arr[:k]
    return arr


arr=[0,0,0,1,2,3,4,5,6,0,0]
print(moveZeros(arr))        


# Sol 2 : (Perfect LeetCode Answer)

def moveZeros(n,  a):
    j = -1
    # Place the pointer j
    for i in range(n):
        if a[i] == 0:
            j = i
            break
    
    # No non-zero elements
    if j == -1:
        return a
    
    # Move the pointers i and j and swap accordingly
    for i in range(j + 1, n):
        if a[i] != 0:
            a[i], a[j] = a[j], a[i]
            j += 1
    
    return a


arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = 10
ans = moveZeros(n, arr)
print(ans)



