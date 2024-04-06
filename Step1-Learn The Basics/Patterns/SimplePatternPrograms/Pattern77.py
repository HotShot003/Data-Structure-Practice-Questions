def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if (i==n//2 and j ==n//2 ):
                print("0",end=" ")
            else :
                    
                print('*',end=' ')
            
            
        print()

pattern(4)        

# * * * * * 
# * * * * *
# * * 0 * *
# * * * * *
# * * * * *        