def pattern(n):
    for i in range(n+1):
        for j in range(2*(n+1)):
            if j < n+1:
                if i+j<=n:
                    print('*',end='')
                else :
                    print(end='')
            else :
                if i-j<=-(5):
                    print('*',end='')
                else :
                    print(end='  ')            
        print() 



pattern(4)                   



# **********
# ****  ****
# ***    ***
# **      **
# *        *