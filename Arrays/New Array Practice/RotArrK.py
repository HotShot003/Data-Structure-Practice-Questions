# # Rotate an array to the right by k steps.


# def Rot(Arr,k):
#     for i in range(k):
#         temp = Arr.pop()     # Remove last element
#         Arr.insert(0, temp)  # Insert at the front
#     return Arr

Arr = list(map(int, input().split()))
k = int(input())
opt = str(input('Rotate l or r : '))

def Rotr(Arr, k):
    n = len(Arr)
    for i in range(k):
        temp = Arr[-1]  # Save last element
        for j in range(n-1, 0, -1):
            Arr[j] = Arr[j-1]  # Shift right
        Arr[0] = temp         # Place last element at front
    return Arr

def Rotl(Arr, k):
    n = len(Arr)
    for i in range(k):
        temp = Arr[0]  # Save first element
        for j in range(0, n-1):
            Arr[j] = Arr[j+1]  # Shift left
        Arr[-1] = temp        # Place first element at end
    return Arr

if opt == 'r':
    print(Rotr(Arr, k))
if opt == 'l':
    print(Rotl(Arr, k))
