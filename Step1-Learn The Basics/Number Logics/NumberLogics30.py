# Write a Program to check whether the number is an Evil Number or Not.

# # Convert a number to binary
# decimal_number = 2
# binary_representation = bin(decimal_number)

# # Print the binary representation
# print(binary_representation) 

# Sol 1 :
def binary(n):
    i=0
    list = []
    
    while n:
        if n%2 == 0:
            list.append(0)
        else:
            list.append(1)
        n = n//2
        i+=1
    # list.reverse()
    return list

# print(binary(25))

def is_EvilNumber(num):
    orgi = num
    l = binary(num)
    c=0
    for i in l :
        if i == 1:
            c+=1
    
    if c%2 == 0:
        return f"{orgi} is a Evil Number" 
    return f"{orgi} is not A Evil Number"


print(is_EvilNumber(10))       
            
            
# Sol 2:



                