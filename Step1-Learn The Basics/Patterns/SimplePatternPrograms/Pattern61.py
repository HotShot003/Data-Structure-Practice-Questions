def pattern(n):
    for i in range(n+1):
        for j in range(2*(n+3)+1):
            if i < 3:
                if j < n+1:
                    if i+j>=3 and j<=4 and i<=1 and i!=j-4:
                        print('*',end='')
                    else:
                        print(end=' ')
                    # if i == 3:
                    #     print('*',end='')    
                else :
                    if i+j>=11 and j<=12 and i<=1 and (j!=12 or i==1):
                        print('*',end='')
                    else:
                        print(end=' ')
            else:
                if i  == 3:
                    print('*',end='')                
        print() 
    # for i in range(3):
    #     for j in range(2*(n+3)+1):
    #             if i==2:                   
    #                     print('*',end='')
    
           
pattern(4)                   


#    *       *   
#   ***     ***

# ***************