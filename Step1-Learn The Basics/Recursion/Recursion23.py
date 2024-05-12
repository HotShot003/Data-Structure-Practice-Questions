# 20.The function f is defined as follows:

# int f (int n) {
# if (n <= 1) return 1;
# else if (n % 2 == 0) return f(n/2);
# else return f(3n - 1);
# }

# Assuming that arbitrarily large integers can be passed as a parameter to the
# function, consider the following statements.
# 1. The function f terminates for finitely many different values of n ≥ 1.
# ii. The function f terminates for infinitely many different values of n ≥ 1.
# iii. The function f does not terminate for finitely many different values of n ≥ 1.
# iv. The function f does not terminate for infinitely many different values of n ≥ 1.
# Which one of the following options is true of the above?
# Options
# A. (i) and (iii)
# B. (i) and (iv)
# C. (ii) and (iii)
# D. (ii) and (iv) (Correct)

def f(n):
    if n <= 1:
        return 1
    elif n % 2 == 0:
        return f(n // 2)
    else:
        return f(3 * n - 1)

print(f(5))