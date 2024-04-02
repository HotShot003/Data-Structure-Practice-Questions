def pattern(n):
    for i in range(2*n+1):
        for j in range(2*n+1):
            if i <n:
                if j <=n:
                    if i + j==n:
                        print(i+1,end='')
                    else :
                        print(end=' ')
                else :
                    if i - j == -n:           
                        print(j-n+1,end='')
                    else :
                        print(end=' ') 
            else :
                if j <n+1:
                    if i-j == n:
                        print(n-j+1,end='')
                    else :
                        print(end=' ')                    
                else :
                    if i+j==n*3:
                        print(j-n+1,end='')
                    else:
                        print(end=' ')    
        print()
        
        
pattern(4)           


#     1    
#    2 2
#   3   3
#  4     4
# 5       5
#  4     4
#   3   3
#    2 2
#     1
