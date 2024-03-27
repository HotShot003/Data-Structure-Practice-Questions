def simplepattern5(n):
    for i in range(2*n+1):
        for j in range(n*2+1):
            
                if (i+j)<n or i-j>n-1//4 or i-j<-(n) or i+j>=3*(2*n+1)//2  :  
                    print('*',end =' ')
                else:
                    print(end='  ')
            
                
        print()

simplepattern5(4)                
# # print()                    
# * * * *   * * * * 
# * * *       * * *
# * *           * *
# *               *

# *               *
# * *           * *
# * * *       * * *
# * * * *   * * * *
