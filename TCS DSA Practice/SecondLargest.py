# Second Largest Num in Arr


arr = list(map(int,input().split()))

# print(arr)

arr.sort()
l = len(arr)
print(arr[l-2])