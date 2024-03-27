def simplepattern9(n):
    for i in range(n+1):
        for j in range(n+1):
            if(i-j)>=0:
                if i<n and j<3:
                    print(i*(i+1)//2+j+1,end=' ')
                else:
                    print(j+2,end=' ')
            else:
                print(end=' ')
        print()            
simplepattern9(4)        

# 1     
# 2 3
# 4 5 6
# 7 8 9 5
# 2 3 4 5 6