# 5.What does fun2() do in general?
# int fun(int x, int y)
# {
# if (y == 0) return 0;
# return (x + fun(x, y-1));
# }
# int fun2(int a, int b)
# {
# if (b == 0) return 1;
# return fun(a, fun2(a, b-1));
# }
# Options
# A. x^y
# B. x+x*y
# C. x*y
# D. x^y (Correct)

def fun(x,y):
    # print(y)
    if y == 0:
        return 0
    return (x + fun(x, y-1))
def fun2(a,b):
    if b == 0:
        return 1
    return fun(a, fun2(a, b-1))

print(fun2(2,3))



# def fun22(a=2,b=2):
#     return a ** b

# print(fun22())

