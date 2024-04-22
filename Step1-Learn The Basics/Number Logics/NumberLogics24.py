# Write a Program to check whether the number is Spy Number or Not.


def digitSum(n):
    s=0
    m=1
    while n :
        s=s+n%10
        m=m*(n%10)
        n=n//10
    return s,m


def spy_Number(n):
    orgi = n
    s,m=digitSum(n)
    if s==m:
        return f"{orgi} is a Spy Number"
    return f"{orgi} is Not a Spy Number"


print(spy_Number(1124))