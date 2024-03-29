def pattern(n):
    for i in range(n+1):
        for j in range (n+1):
            if i+j>=n:
                print(j,end=' ')
            else :
                print(end=' ')
        print()            

pattern(4)

#     4 
#    3 4 
#   2 3 4 
#  1 2 3 4 
# 0 1 2 3 4 