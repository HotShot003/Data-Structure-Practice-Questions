def simplepattern12(n):
    for i in range(n+1):
        for j in range(2*n+1):
            if i+j>=n and j<=(2*n+1)//2  or i-j>=-(n) and j>=(2*n+1)//2  :
                print(chr(65+(i+j-n)),end=' ')
               
            else :
                print(end='  ')    
                
        print()
simplepattern12(4)                

#         A
#       A B C
#     A B C D E
#   A B C D E F G
# A B C D E F G H I