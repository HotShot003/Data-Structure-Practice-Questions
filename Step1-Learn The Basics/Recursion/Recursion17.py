# 14.Consider the following function
# Which one of the following is TRUE?
# int f(int j)
# {
# static int i = 50;
# int k;
# if (i == j)
# {
# printf(“something”);
# k = f(i);
# return 0;
# }
# else return 0;
# }
# Options
# A. The function returns 0 for all values of j.
# B. The function prints the string something for all values of j.
# C. The function returns 0 when j = 50
# D.The function will exhaust the runtime stack or run into an infinite loop when j = 50   (Correct)

def f(j):
    CONS = 50
    if CONS == j:
        print("something")
        k = f(CONS)
        return 0
    else:
        return 0

print(f(50))