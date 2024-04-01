def pattern(n):
    for i in range(n+1):
        for j in range(2*(n+1)):
            if j<n+1:
                if i+j==n+1:
                    print(j,end='')
                else :
                    print(end=' ')
            else :
                if i-j==-(n+1):
                    print(n-i+1,end='')
                else :
                    print(end=' ')                     
        print()

pattern(4)     


#      5    
#     4 4
#    3   3
#   2     2
#  1       1   