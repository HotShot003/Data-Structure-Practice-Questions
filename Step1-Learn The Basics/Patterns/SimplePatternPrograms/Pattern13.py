def simplepattern13(n):
    for i in range(n):
        for j in range(2*n-1):
            if i+j>=n-1 and j<2*n//2  or i-j>(-n) and j>=2*n//2:
                print(chr(65+(j+i-(2*n-1)//2)),end = ' ')
            else :
                print(end ='  ')    
        print()
simplepattern13(4)                


#       A       
#     A B C
#   A B C D E
# A B C D E F G