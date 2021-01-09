# LEETCODE JANUARY CHALLENGE

def arrayStringsAreEqual(word1, word2):
    f1, f2 = "", ""
    for word in word1:
        f1 += word
    for word in word2:
        f2 += word
    
    if f1 == f2: 
        return True
    return False