def pattern(n):
    for i in range(2*n-1):
        for j in range(2*n):
            if i <n:
                if j <n:
                    if i-j>=0:
                        print('*',end=' ')
                    else :
                        print(end='')
                else :
                    if i+j>=2*n-1 :
                        print('*',end=' ')
                    else : 
                        print(end='    ') 
            else :
                if j < n:
                    if i+j<=2*(n-1):
                        print('*',end=' ')
                    else :
                        print(end=' ')
                else :
                    if i-j<=(-1):
                        print('*',end=' ')
                    else :
                        print(end='   ')            
                                           
        print()

pattern(4)                         



# *             * 
# * *         * *
# * * *     * * *
# * * * * * * * *
# * * *     * * *
# * *         * *
# *             *