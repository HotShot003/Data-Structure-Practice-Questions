def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i-j<=0:
                print(chr(65+n-j),end=' ')
            else :
                print(end=' ')
        print()
pattern(4)                    


# E D C B A 
#  D C B A
#   C B A
#    B A
#     A