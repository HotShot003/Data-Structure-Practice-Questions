# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.


def CommonCharac(s):
    dic = dict()
    
    for char in set(words[0]):
        min = float('inf')
        for i in words:
            c = i.count(char)
            if c < min:
                min = c
        dic[char] = min
    
    
    list1 = []
    
    for key , val in dic.items():
        if val > 0:
            for _ in range(val):
                list1.append(key)
    
    return list1

words = ["bella","label","roller"]    

print(CommonCharac(words))            

