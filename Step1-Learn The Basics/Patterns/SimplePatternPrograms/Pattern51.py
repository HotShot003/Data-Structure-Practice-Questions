def pattern(n):
    for i in range(n+1):
        for j in range(2*(n+1)):
            if j < n+1:
                if i-j==0:
                    print(chr(65+j),end='')
                else :
                    print(end=' ')    
            else :
                if i + j==2*n:
                    print(chr(65+i),end='')
                else :
                    print(end=' ')
        print()

pattern(4)



# A       A 
#  B     B
#   C   C
#    D D
#     E                                