def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if (i==4 or j==0) or i-j==0:
                print('*',end=' ')
            else :
                print(end='  ')
        print()

pattern(4)                            

# *
# * *
# *   *
# *     *
# * * * * *