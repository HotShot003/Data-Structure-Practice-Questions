#Method 1:
def ReverseStr(s):
    
    
    return s[::-1]

print(ReverseStr(s='abc'))

#Method 2:

def ReverseStr1(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

print(ReverseStr1(s='cba'))  # Output: abc
