def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i+j>=n or (i==0 and j==4) or (i==2 and j==2) or (i==4 and j==0):
                print('*',end=' ')
            else:
                print(end='  ')
        print()


pattern(5)                    

#         * * 
#         * *
#     * * * *
#     * * * *
# * * * * * *
# * * * * * *