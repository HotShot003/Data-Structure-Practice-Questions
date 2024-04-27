# Write a program to find out all palindrome numbers present within a
# given range.

def reverseNum(s,e):
    palindrome_n = []
    
    for n in range(s,e+1):
        orgi = n
        flag = False
        res = 0
        if n<0:
            flag = True
            n=-n
        while n:
            res = (res * 10 ) + (n%10)
            n=n//10
        reverse_num = res if not flag else -res

        if reverse_num == orgi:
            palindrome_n.append(reverse_num)
    return palindrome_n

# print(reverseNum(-321))        

print(reverseNum(1,30))
