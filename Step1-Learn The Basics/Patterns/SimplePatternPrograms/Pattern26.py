def pattern(n):
    for i in range(n+1):
        for j in range (n+1):
            if i+j>=n:
                print((n-j)-i+n,end=' ')
            else :
                print(end=' ')
        print()            

pattern(4)

#     4 
#    4 3
#   4 3 2
#  4 3 2 1
# 4 3 2 1 0