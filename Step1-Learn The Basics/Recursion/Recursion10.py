# 7.What does the following function do?
# int fun(unsigned int n)
# {
# if (n == 0 || n == 1)
# return n;
# if (n%3 != 0)
# return 0;
# return fun(n/3);
# }
# Options
# A. It returns 1 when n is a multiple of 3, otherwise returns 0
# B. It returns 1 when n is a power of 3, otherwise returns 0
# C. It returns 0 when n is a multiple of 3, otherwise returns 1
# D. It returns 0 when n is a power of 3, otherwise returns 1

# print(3//3)


def fun(n):
    
    if n==0 or n==1:
        return n
    
    if n%3!=0:
        return 0
    return fun(n//3)

print(fun(9))