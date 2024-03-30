def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if (i+j>=n//2 and i-j>=-(n//2)) and (i-j<=(n//2) and i+j<=(n-1)*2):
                print("*",end=" ")
            else:
                print(end="  ")
        print()        
pattern(4)


#   *
#  ***
# *****
#  ***
#   *
#change spaces at line 5,7 and u find diff patterns
#     *     
#   * * *
# * * * * *
#   * * *
#     *