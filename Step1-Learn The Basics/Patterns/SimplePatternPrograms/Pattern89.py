def pattern(n):
    for i in range(2*n):
        for j in range(2*n):
            if i==0 or j==0 or i==2*n-1 or j==2*n-1 or i-j==0 or i+j==2*n-1 :
                print('*',end=' ')
            else :
                print(end='  ')
        print()
        
pattern(4)       

# * * * * * * * * 
# * *         * *
# *   *     *   *
# *     * *     *
# *     * *     *
# *   *     *   *
# * *         * *
# * * * * * * * *    
