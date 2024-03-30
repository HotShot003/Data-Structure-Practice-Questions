def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i-j<=0:
                print(chr(65+(n-i+j-n)),end=' ')
            else :
                print(end=' ')
        print()            

pattern(4)

# A B C D E 
#  A B C D
#   A B C
#    A B
#     A