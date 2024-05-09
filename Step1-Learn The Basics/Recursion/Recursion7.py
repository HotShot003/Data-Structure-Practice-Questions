# 4.What does the following function do?
# int fun(int x, int y)
# {
# if (y == 0) return 0;
# return (x + fun(x, y-1));
# }
# Options
# A. x+y
# B. x+x*y
# C. x*y (correct)
# D. x^y


def fun(x,y):
    
    if y == 0:
        return 0
    return (x + fun(x, y-1))


print(fun(2,3))