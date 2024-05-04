# Write a Python program to convert a decimal number to a binary number.


def binary(n):
    
    # i=0
    list=[]
    while n:
        if n%2 == 0:
            list.append(0)
        else:
            list.append(1)
        n = n//2
        # i+=1
    list.reverse()
    return list


print(binary(5))