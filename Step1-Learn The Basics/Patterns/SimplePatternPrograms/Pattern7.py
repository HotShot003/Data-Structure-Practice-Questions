def simplepattern7(n):
    print("Simple Pattern 7")
    for i in range(n+1):
        for j in range(i+1):
            if i-j>=0:
                print(j+1,end=' ')
            else :
                print(end='')
        print()            
        
        
simplepattern7(4)     

# Simple Pattern 7
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5   