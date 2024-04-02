def pattern(n):
    for i in range(2*n+1):
        for j in range(2*n+1):
            if i < (2*n+1)//2:
                if j <=(2*n+1)//2:
                    if i + j==(2*n+1)//2:
                        print('*',end='')
                    else :
                        print(end=' ')
                else :
                    if i - j == -((2*n+1)//2):           
                        print('*',end='')
                    else :
                        print(end=' ') 
            else :
                if j <n+1:
                    if i-j == (2*n+1)//2:
                        print('*',end='')
                    else :
                        print(end=' ')                    
                else :
                    if i+j==n*3:
                        print('*',end='')
                    else:
                        print(end=' ')    
        print()
        
        
pattern(4)           


#     *    
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *                  