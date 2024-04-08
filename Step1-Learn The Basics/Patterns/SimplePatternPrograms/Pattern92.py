def pattern(n):
    for i in range(2*n+1):
        for j in range(2*n+1):
            if i<n+1:
                if i - j == -n or i == n:
                    print('*',end=' ')
                else:
                    print(end='  ')
            else :
                if i+j==12:
                    print('*',end=' ')
                else :
                    print(end='  ')            
       
        print()
        
pattern(4)                    

#         *
#           *
#             *
#               *
# * * * * * * * * *
#               *
#             *
#           *
#         *