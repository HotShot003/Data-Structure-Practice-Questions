# 6.Output of following program?
# #include<stdio.h>
# void print(int n)
# {
# if (n > 4000)
# return;
# printf("%d ", n);
# print(2*n);
# printf("%d ", n);
# }
# int main()
# {
# print(1000);
# getchar();
# return 0;
# }
# Options
# A. 1000 2000 4000
# B. 1000 2000 4000 4000 2000 1000 (Correct)
# C. 1000 2000 4000 2000 1000
# D. 1000 2000 2000 1000


def printf(n):
    if n > 4000:
        return
    print(n,end=' ')
    printf(2 * n)
    print(n,end=' ')

printf(1000)