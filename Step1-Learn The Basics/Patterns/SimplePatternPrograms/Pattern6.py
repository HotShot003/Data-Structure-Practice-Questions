def simplepattern6(n):
    for i in range((n-1)*2+1):
        for j in range((n-1)*2+1):
            if i+j==n-1 or i-j==n-1 or i-j==-(n-1) or i+j==n*2+1:
                print('*',end=' ')
            else:
                print(end='  ')    
        print()
simplepattern6(4)       

#       *       
#     *   *
#   *       *
# *           *
#   *       *
#     *   *
#       *        