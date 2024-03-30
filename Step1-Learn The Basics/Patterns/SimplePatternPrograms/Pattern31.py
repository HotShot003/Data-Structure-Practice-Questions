
def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i-j<=0:
                print(n-j+1,end=' ')
            else :
                print(end=' ')
        print()            

pattern(4)

# 5 4 3 2 1 
#  4 3 2 1
#   3 2 1
#    2 1
#     1