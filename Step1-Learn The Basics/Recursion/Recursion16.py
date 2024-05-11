# 13.Consider the following function
# Give a value q (to 2 decimals) such that f(q) will return q:_____.
# double f(double x){
# if (abs(x*x - 3) < 0.01) return x;
# else return f(x/2 + 1.5/x);
# }
# Options
# A. 1.73
# B. 2.24
# C. 4.22
# D. 3.42


def f(x):
    if abs(x*x - 3) < 0.01:
        return x
    else:
        return f(x/2 + 1.5/x)

print(f(3))

# if abs(1.73 * 1.73 - 3) < 0.01:
#     print(True)