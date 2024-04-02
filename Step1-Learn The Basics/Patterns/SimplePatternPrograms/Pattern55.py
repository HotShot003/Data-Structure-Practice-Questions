def pattern(n):
    for i in range(2*n+1):
        for j in range(2*n+1):
            if i <n:
                if j <=n:
                    if i + j==n:
                        print(n-i+1,end='')
                    else :
                        print(end=' ')
                else :
                    if i - j == -n:           
                        print(n-i+1,end='')
                    else :
                        print(end=' ') 
            else :
                if j <n+1:
                    if i-j == n:
                        print(i-n+1,end='')
                    else :
                        print(end=' ')                    
                else :
                    if i+j==n*3:
                        print(i-n+1,end='')
                    else:
                        print(end=' ')    
        print()
        
        
pattern(4)           



#     5    
#    4 4
#   3   3
#  2     2
# 1       1
#  2     2
#   3   3
#    4 4
#     5
