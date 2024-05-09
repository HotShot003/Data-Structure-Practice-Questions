
# 1. Predict output of following program
# #include <stdio.h>
# int fun(int n)
# {
# if (n == 4)
# return n;
# else return 2 * fun ( n+1 );
# }
# int main()
# {
# printf("%d ", fun(2));
# return 0;
# }
# Options
# A.4
# B. 8
# C. 16 (correct)
# D.Runtime Error

# Python Code:

def func(n):
    
    if n == 4:
        return n
    return 2 * func(n+1)

print(func(2))