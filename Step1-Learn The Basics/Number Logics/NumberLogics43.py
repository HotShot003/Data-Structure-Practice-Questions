# Write a Program to Find out all Happy numbers present within a given
# range.

def sqr(n):
    return n * n
# print(sqr(10))

def range_HappyNum(s,e):
    hppynum=[]
    
    for n in range(s,e+1):
        orgi = n
        seen_num=set()
        curr_num=n
        
        while curr_num!=1 and curr_num not in seen_num:
            seen_num.add(curr_num)
            next_num=0
            
            while curr_num > 0:
                next_num = next_num + sqr(curr_num % 10)
                curr_num =curr_num // 10
            
            curr_num = next_num 
        # print(curr_num)
        if curr_num == True:
            hppynum.append(orgi)
        
    return hppynum    


print(range_HappyNum(1,100))
    
    