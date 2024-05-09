# 2. Consider the following recursive function fun(x, y). What is the value of
# fun(4, 3)
# int fun(int x, int y)
# {
# if (x == 0)
# return y;
# return fun(x - 1, x + y);
# }
# Options
# A.13 (correct)
# B. 8
# C. 9
# D.Runtime Error


def fun(x,y):
    if x==0:
        return y
    
    return fun(x-1,x+y)

print(fun(4,3))