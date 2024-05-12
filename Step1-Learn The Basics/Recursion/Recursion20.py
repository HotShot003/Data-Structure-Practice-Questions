# 17.Consider the following C function.
# int fun (int n)
# {
# int x=1, k;
# if (n==1) return x;
# for (k=1; k<n; ++k)
# x = x + fun(k) * fun(n – k);
# return x;
# }
# The return value of fun(5) is __________.
# Options
# A. 0
# B. 26
# C.51  (Correct)
# D.71

def fun(n):
    x = 1
    if n == 1:
        return x
    for k in range(1, n):
        x = x + fun(k) * fun(n - k)
    return x

print(fun(5))