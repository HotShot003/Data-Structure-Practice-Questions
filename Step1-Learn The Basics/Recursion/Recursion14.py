# 11.Predict the output of following program
# #include<stdio.h>
# int f(int *a, int n)
# {
# if(n <= 0) return 0;
# else if(*a % 2 == 0) return *a + f(a+1, n-1);
# else return *a - f(a+1, n-1);
# }
# int main()
# {
# int a[] = {12, 7, 13, 4, 11, 6};
# printf("%d", f(a, 6));
# getchar();
# return 0;
# }
# Options
# A. -9
# B. 5
# C. 15 (Correct)
# D. 19

def f(a,n):
    if n <= 0:
        return 0
    elif a[0]%2 == 0:
        return a[0] + f(a[1:],n-1)
    else :
        return a[0] - f(a[1:],n-1)
    
a=[12,7,13,4,11,6]

print(f(a,6))
print(a[1:])