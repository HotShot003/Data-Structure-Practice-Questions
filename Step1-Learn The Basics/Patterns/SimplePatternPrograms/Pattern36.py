def pattern(n):
    for i in range(2*n+1):
        for j in range(n+1):
            if i < n :
                if i+j>=n and i-j>=-(n):
                    print(i+1,end=' ')
                else :
                    print(end=' ')
            else :
                if i-j<=n and i+j<=n*3:
                    print(n-i+n+1,end=' ')
                else:
                    print(end=' ')            
        print()                
            



pattern(4)

#     1 
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5
#  4 4 4 4
#   3 3 3
#    2 2
#     1
