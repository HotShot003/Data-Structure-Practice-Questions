def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i-j>n//2 or (j==0 and i in [0,1]) or (i in [2,3] and j in [0,1]) or (i==4 and j==2):
                print('*',end=' ')
            else :
                print(end='')    
        #     if i+j>=n :
        #         if i in [1,2,3,4,5] and j in [5,2]:
        #             if i==5 and j<3:
                        # print(j,end=' ')
        #             print(end='')
        #         else :    
        #             print('*',end=' ')
        #     else :
        #         print(end='')
        print()

pattern(5)           


# * 
# *
# * *
# * *
# * * *
# * * *         