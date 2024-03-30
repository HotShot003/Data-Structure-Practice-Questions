def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i-j<=0:
                print(chr(65+n-i),end=' ')
            else :
                print(end=' ')
        print()

pattern(4)

# E E E E E 
#  D D D D 
#   C C C 
#    B B 
#     A                     