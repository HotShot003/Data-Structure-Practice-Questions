def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i-j==0 or i+j==n:
                print(chr(65+i),end=' ')
            else:
                print(end='  ')
        print()

pattern(4)                    


# A       A 
#   B   B
#     C
#   D   D
# E       E
