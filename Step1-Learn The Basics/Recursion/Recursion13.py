# unsigned int foo(unsigned int n, unsigned int r) {
# if (n > 0) return (n%r + foo (n/r, r ));
# else return 0;
# }
# What is the return value of the function foo when it is called as foo(513, 2)?
# Options
# A. 9
# B. 8 
# C. 5
# D. 2 (Correct)


def foo(n,r):
    if n > 0:
        return (n%r + foo (n//r, r ))
    return 0


print(foo(513,2))