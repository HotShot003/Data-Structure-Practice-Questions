def pattern(n):
    for i in range(n+1):
        for j in range(n+1):
            if i==2 or j==2:
                print('*',end=' ')
            else :
                # print(end='  ')
                print('o',end=' ')
        print()

pattern(4)                    

