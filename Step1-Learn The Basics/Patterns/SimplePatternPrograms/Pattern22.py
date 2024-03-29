def pattern(n):
    for i in range(2*(n-1)+1):
        for j in range(n):
            if i<n:
                if i+j>=n-1:
                    print(chr(65+j),end=' ')
                else :
                    print(end='  ')    
            else :
                if i-j<n:
                    print(chr(65+j),end=' ')
                else :
                    print(end='  ')
        print()            
pattern(4)                            

#       D 
#     C D
#   B C D
# A B C D
#   B C D
#     C D
#       D   