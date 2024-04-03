def pattern(n):
    f=1
    for i in range(2*(n+1)):
        for j in range(2*(n+1)):
            if i+j>=2*(n+1)-1:
                if (i==5 and j in [6,7]) or (i==6 and j==6):
                    f=0
                    print(end='  ')
                    
                if f == 1:    
                    print('*',end=' ')
                f=1    
            else:
                print(end=' ')
            
        print()
pattern(4)                    


#          * 
#         * *
#        * * *
#       * * * *
#      * * * * *
#     * *     * *
#    * * *   * * *
#   * * * * * * * *
#  * * * * * * * * *
# * * * * * * * * * *