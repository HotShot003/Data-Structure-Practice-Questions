def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if j<=1:
                if i-j>=0:       
                    print(j,end=' ')
                else :
                    print(end='')
            else :
                if i-j>=0:       
                    print(j-1,end=' ')
                else :
                    print(end='')
                            
        print()            
pattern(4)      


# 0 
# 0 1
# 0 1 1
# 0 1 1 2
# 0 1 1 2 3  