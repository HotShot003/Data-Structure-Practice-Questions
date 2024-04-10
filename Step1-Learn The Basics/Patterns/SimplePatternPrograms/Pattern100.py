def pattern(n):
    for i in range(n+1):
        for j in range(5*n):
            if i-j==0 or i+j==4 or i-j==-5 or i+j==9 or i-j==-10 or i+j==14 or i-j==-15 or i+j==19:
                print("*",end=" ")
            else:
                print(end='  ')
        print()
pattern(4)                    
        
        
# *       * *       * *       * *       * 
#   *   *     *   *     *   *     *   *
#     *         *         *         *
#   *   *     *   *     *   *     *   *
# *       * *       * *       * *       *        