def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i-j<=0:
                print(n-i+1,end=' ')
            else :
                print(end=' ')
        print()    
        
pattern(4)                


# 5 5 5 5 5 
#  4 4 4 4 
#   3 3 3 
#    2 2 
#     1 