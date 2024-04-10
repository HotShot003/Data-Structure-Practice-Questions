def pattern(n):
    for i in range(n+1):
        for j in range(2*n-1):
            if (j%3!=0 and i==0) or (j%3==0 and i==1) or i-j==1 or i+j==7:
                print('*',end=' ')
            else :
                print(end='  ')
        print()
pattern(4)                    

#   * *   * *   
# *     *     *
#   *       *
#     *   *
#       *