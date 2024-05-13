# 19. Recursive Implementation of atoi()
# The atoi() function takes a string (which represents an integer) as an argument and
# returns its value.
# Examples:
# Input:
# char str[] = "112";
# Output:
# 112


def atoi(string):
    
    s = int(string)
    
    return s

str = '12122'
print(type(str))  # class str
print(type(atoi(str))) # class int
print(atoi(str))