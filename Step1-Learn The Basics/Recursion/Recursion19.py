# 16.Consider the following Function
# int f(int n)
# {
# static int i = 1;
# if (n >= 5)
# return n;
# n = n+i;
# i++;
# return f(n);
# }
# The value returned by f(1) is
# Options
# A. 5
# B. 6
# C. 7
# D. 8


# Mistakely Created Question

# The variable i is reinitialized to 1 every time the function is called. This means that i will always be 1 when n is incremented, and i itself will never be more than 2. Because i doesn’t retain its value across function calls, the function doesn’t behave as expected.

def f1(n):
    i=1
    if n >= 5:
        return n
    n = n + i
    i += 1
    return f1(n)
print(f1(1))  # returns 5

# Proper Convet to Python
def f(n, i=1):
    if n >= 5:
        return n
    n = n + i
    i += 1
    return f(n, i)
print(f(1))