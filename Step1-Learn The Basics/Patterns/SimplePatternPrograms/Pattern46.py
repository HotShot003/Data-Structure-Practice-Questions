def pattern(n):
    for i in range(n+1):
        for j in range(2*(n+1)):
            if j < n+1:
                if i+j==n+1:
                    print(chr(65 + i), end="")
                else :
                    print(end=" ")    
            else :
                if i-j==-(n+1):
                    print(chr(65+i),end='')
                else :
                    print(end=' ')
        print() 


pattern(4)
         
#      A    
#     B B   
#    C   C  
#   D     D 
#  E       E                               