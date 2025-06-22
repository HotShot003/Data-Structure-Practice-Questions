# Count the frequency of each element in an array.


Arr = list(map(int,input().split()))

def CountFrequency(Arr):
    dic = dict()
    for i in Arr:

        if i in dic:
            dic[i]+=1
        else :
            dic[i] = 1
                        
    return dic

print(CountFrequency(Arr))                    