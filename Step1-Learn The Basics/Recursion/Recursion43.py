# 21. Write a recursive function that, given a string s, prints the characters
# of s in reverse order.
# Examples:
# Input:
# char ch[] = “hello”
# Output:
# olleh

def rev(a):
    
    if len(a) == 0:
        return
    else:
        print(a[-1], end = "")
        rev(a[0:len(a)-1])

print(rev('hello'))        