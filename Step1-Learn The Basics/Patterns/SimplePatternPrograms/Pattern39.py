def pattern(n):
    for i in range(2*n+1):
        for j in range(n+1):
            if i <n :
                if i+j>=n:
                    print(i+j-(n-1),end=' ')
                else :
                    print(end=' ')
            else :
                if i-j<=n :
                    print(j+1,end=' ')
                else:
                    print(end=' ')            
        print()                
pattern(4)       

# and i-j>=-(n) line 5
# and i+j<=n*3 line 10


#     1 
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
#  2 3 4 5
#   3 4 5
#    4 5
#     5