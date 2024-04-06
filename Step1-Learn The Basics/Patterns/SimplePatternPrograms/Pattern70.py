def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i-j==0 or i+j==n:
                if i-j==0 or i+j==n:
                    print('o',end=' ')
                else:
                    print(end='  ')
            else:        
                print('*',end=' ')
                
        print()

pattern(4)         

# o * * * o 
# * o * o *
# * * o * *
# * o * o *
# o * * * o           

