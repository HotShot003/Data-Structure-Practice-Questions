# Write a program to check the given number is a palindrome or not.

def rev(n):
    res = 0
    while n :
        res = (res * 10) + (n%10)
        n=n//10
    return res

# print(rev(321))  

def palindrome(n):
    if n == rev(n):
        return f"{n} is a Palindrome Number"
    else:
        return f"{n} is not a Palindrome Number"

print(palindrome(123)) 
        