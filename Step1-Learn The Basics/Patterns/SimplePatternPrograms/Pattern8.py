def simplepattern8(n):
    for i in range(n+1):
        for j in range(n+1):
            if(i-j)>=0:
                print(i*(i+1)//2+j+1,end=' ')
            else:
                print(end=' ')
        print()            
simplepattern8(4)        

# 1     
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15