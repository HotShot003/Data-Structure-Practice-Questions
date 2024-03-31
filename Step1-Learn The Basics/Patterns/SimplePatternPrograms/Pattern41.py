def pattern(n):
    for i in range(2*n+1):
        for j in range(n+1):
            if i< n:
                if i+j>=n:
                    print(chr(65+i),end=' ')
                else :
                    print(end=' ')
            else :
                if i-j<=n:
                    print(chr(65+(n-i)+(2*n//2)),end=' ')
                else :
                    print(end=' ')
        print()

pattern(4)                                    

#     A 
#    B B
#   C C C
#  D D D D
# E E E E E
#  D D D D
#   C C C
#    B B
#     A