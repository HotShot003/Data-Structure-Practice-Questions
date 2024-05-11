# 9.Consider the following recursive C function that takes two arguments
# unsigned int foo(unsigned int n, unsigned int r) {
# if (n > 0) return (n%r + foo (n/r, r ));
# else return 0;
# }
# What is the return value of the function foo when it is called as foo(345, 10) ?
# Options
# A. 345
# B. 12 (Correct)
# C. 5
# D. 3

def foo(n,r):
    if n > 0:
        return (n%r + foo (n//r, r ))
    return 0


# print(1//2)
print(foo(345,10))