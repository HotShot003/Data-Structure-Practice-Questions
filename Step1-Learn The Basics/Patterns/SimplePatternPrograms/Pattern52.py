def pattern(n):
    for i in range(n+1):
        for j in range(2*(n+1)):
            if j < n+1:
                if i-j==0:
                    print(chr(65+n-j),end='')
                else :
                    print(end=' ')    
            else :
                if i+j==2*n:
                    print(chr(65+n-i),end='')
                else :
                    print(end=' ')
        print()


pattern(4)                                


# E       E 
#  D     D
#   C   C
#    B B
#     A