def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i+j>=n:
                print(chr(65+(i+j-n)),end=' ')
            else:
                print(end=' ')
        print()
        
pattern(4)                    

#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 