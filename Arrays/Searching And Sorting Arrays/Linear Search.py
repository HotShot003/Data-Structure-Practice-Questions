# Implement linear search to find an element in an unsorted array.

def LinearSearch(Arr,val):

    for i in range(len(Arr)):
        if Arr[i] == val:
            return i

    return print('Not Found in Array')    

Arr = list(map(int,input().split()))
val = int(input('Enter Val To Search : '))


if LinearSearch(Arr,val) is None:
    pass
else :
    print(LinearSearch(Arr,val))