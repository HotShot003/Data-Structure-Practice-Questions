def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i+j>=n:
                print(chr(i+65),end=' ')
            else:
                print(end=' ')
        print()
        
pattern(4)                    



#     A 
#    B B 
#   C C C 
#  D D D D 
# E E E E E 