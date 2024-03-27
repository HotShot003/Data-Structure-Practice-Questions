def simplepattern11(n):
    for i in range(n+1):
        for j in range(n+1):
            if i+j<=n:
                print(chr(65+(i)),end=(' '))
            else:
                print(end=' ')
        print()
simplepattern11(4)                    

# A A A A A 
# B B B B
# C C C
# D D
# E