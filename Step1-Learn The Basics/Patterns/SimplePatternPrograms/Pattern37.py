def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if (i== 0 and j <=n-(n//2)) or (j==n//2 or i == n//2) or (j==n and  i<= n//2) or(j==0 and i>=n//2) or(i==n and j>=n//2):
                print('* ',end='')
            else :
                print(end='  ')    
        print()    

n=3
if n%2==0:
    pattern(n)
else :
    n+=1
    pattern(n)    
# pattern(4)

# * * *   * 
#     *   *
# * * * * *
# *   *
# *   * * *          