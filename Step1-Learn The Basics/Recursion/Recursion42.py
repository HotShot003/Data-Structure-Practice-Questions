# 20. Check if a number is Palindrome
# Given an integer, write a function that returns true if the given number is palindrome,
# else false. For example, 12321 is palindrome, but 1451 is not palindrome.
# Examples:
# Input:
# int = 11211;
# Output:
# Palindrom
# Input:
# int = 12345;
# Output:
# Not a Palindrom

def is_palindrome(num):
    # Convert the number to a string
    str_num = str(num)  

    # Base case: if the string has less than 2 characters, it's a palindrome
    if len(str_num) < 2:
        return 'Yes Palindrome'

    # If the first and last characters of the string are the same,
    # make a recursive call with the middle part of the string
    if str_num[0] == str_num[-1]:
        return is_palindrome(str_num[1:-1])

    # If the first and last characters of the string are not the same, it's not a palindrome
    return 'Not a Palindrome'


print(is_palindrome(121))
# str_num =[1,2,1]
# print(str_num[1:-1])