# Solution 1

# def pattern(n):
#     for i in range(2*n+1):
#         for j in range(n+1):
#             if i < n :
#                 if i+j>=n and i-j>=-(n):
#                     print('*',end=' ')
#                 else :
#                     print(end=' ')
#             else :
#                 if i-j<=n and i+j<=n*3:
#                     print('*',end=' ')
#                 else:
#                     print(end=' ')            
#         print()                
# pattern(4)       


# Solution 2

def pattern(n):
    for i in range(2*n+1):
        for j in range(n+1):
            if i < n :
                if i+j>=n:
                    print('*',end=' ')
                else :
                    print(end=' ')
            else :
                if i-j<=n :
                    print('*',end=' ')
                else:
                    print(end=' ')            
        print()                
pattern(4)       


#     * 
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *