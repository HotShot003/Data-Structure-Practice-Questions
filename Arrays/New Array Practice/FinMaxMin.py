# Find the maximum and minimum elements in an array.

# Jugad No. 1

# def MaxMin(Arr,opt):
    
#     Arr.sort()

#     if opt == 'Max':
#         return Arr[-1]
#     else :
#         return Arr[0]

# Arr = list(map(int,input().split()))
# opt = input('Max or Min : ')
# print(MaxMin(Arr,opt))

#Proper Answered Code :

def MinMax(Arr):
    max = min = Arr[0]

    for i in Arr[1:]:

        if i > max :
            max = i

        if i < min :
            min = i

    return max , min 

Arr = list(map(int,input().split()))

max , min = MinMax(Arr)

print(f'Maximum is: {max} and Minimum is: {min}')