def word():
    s = input()
    cu, cl = 0, 0
    for i in s:
        if i.isupper() :
            cu += 1
        else: 
            cl += 1
    if cu > cl :
        return s.upper()
    else:
        return s.lower()


print(word())