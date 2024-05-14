# 22. Function to copy string (Recursive)
# Given two strings, copy one string to other using recursion. 
# Examples:
# Input:
# s1 = "hello"
# s2 = "geeksforgeeks"
# Output:
# s2 = "hello"


def copy_string(s1, s2, index=0):
    # Base case: if the index is equal to the length of s1, return s2
    if index == len(s1):
        return s2[:index]

    # Recursive case: replace the character at the current index in s2 with the character from s1
    # Then make a recursive call with the next index
    s2 = s2[:index] + s1[index] + s2[index+1:]
    return copy_string(s1, s2, index + 1)

s1 = 'hello'
s2 = 'geeksforgeeks'

print(copy_string(s1, s2))  # Output: "hello"
