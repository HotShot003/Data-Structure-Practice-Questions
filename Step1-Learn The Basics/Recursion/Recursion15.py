# #include <stdio.h>
# int fun(int n, int *f_p)
# {
# int t, f;
# if (n <= 1)
# {
# *f_p = 1;
# return 1;
# }
# t = fun(n- 1,f_p);
# f = t+ * f_p;
# *f_p = t;
# return f;
# }
# int main()
# {
# int x = 15;
# printf (" %d n", fun(5, &x));
# return 0;
# }
# Options
# A. 6
# B. 8 (Correct)
# C. 14
# D. 15

def fun(n, f_p):
    if n <= 1:
        f_p[0] = 1
        return 1
    t = fun(n - 1, f_p)
    f = t + f_p[0]
    f_p[0] = t
    return f

f_p = [15]
print(fun(5, f_p))
