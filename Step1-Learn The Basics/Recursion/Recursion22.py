# 19.What will be the output of the following C program?
# void count(int n)
# {
# static int d = 1;
# printf("%d ", n);
# printf("%d ", d);
# d++;
# if(n > 1) count(n-1);
# printf("%d ", d);
# }
# int main()
# {
# count(3);
# }
# Options
# A. 3 1 2 2 1 3 4 4 4  (Correct)
# B. 3 1 2 1 1 1 2 2 2
# C.3 1 2 2 1 3 4
# D.3 1 2 1 1 1 2

def count(n, d=[1]):
    print(n, end=" ")
    print(d[0], end=" ")
    d[0] += 1
    if n > 1:
        count(n-1, d)
    print(d[0], end=" ")

def main():
    count(3)

main()
