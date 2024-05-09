# 3.What does the following function print for n = 25?
# void fun(int n)
# {
# if (n == 0)
# return;
# printf("%d", n%2);
# fun(n/2);
# }
# Options
# A.11001
# B. 10011 (correct)
# C. 11111
# D.00000

def fun(n):
    if n == 0:
        return 
    print(n % 2, end="")
    fun(n // 2)


print(fun(25))