# Write a Program to check whether the number is Sunny Number or Not.

def perfectSq(n):
    i=2
    while i*i<=n:
        if i*i==n:
            return True
        i+=1
    return False

# print(perfectSq(4))

def is_SunnyNumber(n):
    orgi = n
    
    num = perfectSq(n+1)
    # print(num)
    
    if num:
        return f"{orgi} is a Sunny Number"
    return f'{orgi} is not a Sunny Number'


print(is_SunnyNumber(24))