# Write a program to check whether a given number is a Harshad number
# or not.


def digitSum(n):
    sum = 0
    while n:
        sum=sum + (n%10)
        n=n//10
    return sum
# print(digitSum(18))

def HarshadNumber(n):
    orgi = n
    
    if n%digitSum(n) == 0:
        return f"{orgi} is a Harshad Number"
    
    return f"{orgi} is Not a Harshad Number"


print(HarshadNumber(18))
