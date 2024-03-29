def pattern(n):
    for i in range(2*(n-1)+1):
        for j in range(n):
            if i<n:
                if i+j>=n-1:
                    print(n-j-i+2,end=' ')
                else :
                    print(end='  ')    
            else :
                if i-j<n:
                    print(i-j,end=' ')
                else :
                    print(end='  ')
        print()            
pattern(4)                            
            

#       3 
#     3 2 
#   3 2 1 
# 3 2 1 0 
#   3 2 1 
#     3 2 
#       3     