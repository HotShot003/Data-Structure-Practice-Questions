def pattern(n):
    for i in range(2*n+1):
        for j in range(2*n+1):
            if (i-j==1 and i<=n+1) or (i+j==9 and i<=n+1) or j==4 or(i==0 and (j in [1,7])):
                print('*',end='')
            else :
                print(end=' ')
        print()

pattern(4)                    


#Trident
#  *  *  * 
# *   *   *
#  *  *  *
#   * * *
#    ***
#     *
#     *
#     *
#     *