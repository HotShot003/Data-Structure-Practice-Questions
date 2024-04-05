def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i-j==0 or i+j==n:
                print(j+1,end=' ')
            else:
                print(end='  ')
        print()

pattern(4)

# 1       5 
#   2   4
#     3
#   2   4
# 1       5