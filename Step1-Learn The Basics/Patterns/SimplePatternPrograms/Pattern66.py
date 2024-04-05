def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i-j==0 or i+j==n:
                print(n-j+1,end=' ')
            else:
                print(end='  ')
        print()

pattern(4)                    

# 5       1 
#   4   2
#     3
#   4   2
# 5       1