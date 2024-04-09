def pattern(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            if (i+j>=3 and i-j>=-3) and (i-j<=3) and (i+j<=9):
                if i==3 and j == 3:
                    print('O',end=' ')
                else :    
                    print('*',end=' ')
            else :
                print(end='  ')
        print()

pattern(4)      


#       *       
#     * * *
#   * * * * *
# * * * O * * *
#   * * * * *
#     * * *
#       *              