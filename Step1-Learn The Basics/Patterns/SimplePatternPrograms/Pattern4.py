def simplepattern4(n):
    for i in range(n+1):
        for j in range(n+1):
            if i-j<=0:
                print('*',end=' ')
            else :
                print(end='  ')
        print()
        
simplepattern4(4)                           

# * * * * * 
#   * * * *
#     * * *
#       * *
#         *