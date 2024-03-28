def pattern(n):
    for i in range(2*(n-1)+1):
        for j in range(n):
            if i<n:
                if  i-j>=0:
                    print('*',end=' ')
                else : print(end='')
            else :
                if i+j<2*(n-1)+1:
                    print('*',end=' ')
                else :print(end='')
                        
        print() 
        
pattern(4)               


# *
# * *
# * * *
# * * * *
# * * *
# * *
# *