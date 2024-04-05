def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i-j==0 or i+j==n:
                print(chr(65+j),end=' ')
            else:
                print(end='  ')
        print()

pattern(4)                    


# A       E 
#   B   D
#     C
#   B   D
# A       E