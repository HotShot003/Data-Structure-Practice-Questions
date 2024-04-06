def pattern(n):
    for i in range(2*n-2):
        for j in range(2*n+1):
            if i+j>=n+1 and i+j<=2*n:
                print('*',end=' ')
            else :
                print(end='  ')
        print()        

pattern(4)  


#          * * * * 
#         * * * *
#       * * * *
#     * * * *
#   * * * *
# * * * *      