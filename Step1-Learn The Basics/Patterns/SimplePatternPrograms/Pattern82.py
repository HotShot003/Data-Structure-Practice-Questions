def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i-j<=0  or (i==1 or j==5) or (i==3 and j==2) or (i==5 and j==1):
                print('*',end=' ')
            else:
                print(end='')
        print()
 
pattern(5)

# * * * * * * 
# * * * * * *
# * * * *
# * * * *
# * *
# * *                   
