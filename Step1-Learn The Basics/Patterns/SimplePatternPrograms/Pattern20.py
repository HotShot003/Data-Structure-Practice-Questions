# def pattern6(n):
#     for i in range(2*(n-1)+1):
#         for j in range(n):
#             if i<=2*(n-1)//2:
#                 if i+j>=2*(n-1)//2 and i<=2*(n-1)//2:
#                     print(2*(n-1)//2-j-i+(2*(n-1)//2),end=" ")
#                 else :
#                     print(end="  ")
#             else :
#                 if i-j<=(2*(n-1))//2:
#                     print(i-j,end=' ')
#                 else :
#                     print(end='  ')
                                
#         print()

# pattern6(4)     

def pattern(n):
    for i in range(2*(n-1)+1):
        for j in range(n):
            if i<n:
                if i+j>=n-1:
                    print(j,end=' ')
                else :
                    print(end='  ')    
            else :
                if i-j<n:
                    print(j,end=' ')
                else :
                    print(end='  ')
        print()            
pattern(4)                            
            
            
#       3 
#     2 3
#   1 2 3
# 0 1 2 3
#   1 2 3
#     2 3
#       3           