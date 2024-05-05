# Write a program to Find the nth palindrome number.


def is_PalindromeNumber(n):
    if n < 0:
        return False

    temp = n
    rev = 0

    while temp > 0:
        rev = rev * 10 + temp % 10
        temp = temp // 10

    if n == rev:
        return True
    else:
        return False
    

def nth_PalindromeNumber(n):
    count = 0
    curr_num = 1    
    
    while count < n:
        if is_PalindromeNumber(curr_num):
            count += 1
        if count == n :
            return curr_num
        curr_num += 1

    return curr_num - 1

print(nth_PalindromeNumber(11))