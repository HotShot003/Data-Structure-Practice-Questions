def pattern(n):
    for i in range(2*n+1):
        for j in range(n+1):
            if i< n:
                if i+j>=n:
                    print(chr(65+(j+i-n)),end=' ')
                else :
                    print(end=' ')
            else :
                if i-j<=n:
                    print(chr(65+(j)),end=' ')
                else :
                    print(end=' ')
        print()

pattern(4)                                    

#     A 
#    A B
#   A B C
#  A B C D
# A B C D E
#  B C D E
#   C D E
#    D E
#     E