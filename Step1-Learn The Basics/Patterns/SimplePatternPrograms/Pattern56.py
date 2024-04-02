def pattern(n):
    for i in range(2*n+1):
        for j in range(2*n+1):
            if i<n:
                if j<=n:
                    if i + j==n:
                        print(chr(65+n-i),end='')
                    else :
                        print(end=' ')
                else :
                    if i - j == -n:           
                        print(chr(65+n-i),end='')
                    else :
                        print(end=' ') 
            else :
                if j <n+1:
                    if i-j == n:
                        print(chr(65+(i-n)),end='')
                    else :
                        print(end=' ')                    
                else :
                    if i+j==n*3:
                        print(chr(65+i-n),end='')
                    else:
                        print(end=' ')    
        print()
        
        
pattern(4)           



#     E    
#    D D
#   C   C
#  B     B
# A       A
#  B     B
#   C   C
#    D D
#     E