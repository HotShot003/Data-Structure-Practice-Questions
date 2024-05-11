# 15.Consider the following Program
# Which one of the following is Correct Output?
# #include<stdio.h>
# void crazy(int n,int a,int b)
# {
# if (n <= 0) return;
# crazy(n-1, a, b+n);
# printf("%d %d %dn",n,a,b);
# crazy(n-1, b, a+n);
# }
# int main()
# {
# crazy(3,4,5);
# return 0;
# }
# Options
# A.       (Correct )
# 1 4 10
# 2 4 8
# 1 8 6
# 3 4 5
# 1 5 9
# 2 5 7
# 1 7 7
# B.
# 3 4 5
# 1 4 10
# 2 4 8
# 1 8 6
# 1 5 9
# 2 5 7
# 1 7 7
# C.
# 1 4 10
# 2 4 8
# 1 8 6
# 3 4 5
# D.
# 3 4 5
# 1 5 9
# 2 5 7
# 1 7 7


def crazy(n,a,b):
    if n <= 0 :
        return
    crazy(n-1, a, b+n)
    print(n,a,b)
    crazy(n-1, b, a+n)

crazy(3,4,5)