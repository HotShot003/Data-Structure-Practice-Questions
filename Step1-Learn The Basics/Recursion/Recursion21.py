# 18.Consider the following recursive C function. If get(6) function is being
# called in main() then how many times will the get() function be invoked
# before returning to the main()?
# void get (int n)
# {
# if (n < 1) return;
# get(n-1);
# get(n-3);
# printf("%d", n);
# }
# Options
# A. 15
# B. 25 (Correct)
# C.35
# D.45

def get(n):
    if n < 1:
        return
    get(n-1)
    print(n)
    get(n-3)


get(6)