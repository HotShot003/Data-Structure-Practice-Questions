def pattern(n):
    for i in range(2*n):
        for j in range(2*n):
            if i+j<=n-1 or i-j<=-(n-1) or i-j>=n-1 or i+j>=2*n+(n-1):
                print('*',end=' ')
            else :
                print(end='  ')
        print()

pattern(4)           


# * * * * * * * * 
# * * *   * * * *
# * *       * * *
# *           * *
# * *           *
# * * *       * *
# * * * *   * * *
# * * * * * * * *         
