# Write a Program to check whether the number is a Trimorphic Number or
# Not.

def cube(n):
    return n * n * n 

def Trimorphic_Number(num):
    orgi = num
    num = cube(num)
    
    if orgi%10 == num%10:
        return f"{orgi} is a Trimorphic Number"
    return f"{orgi} is a Not Trimorphic Number"

print(Trimorphic_Number(249))