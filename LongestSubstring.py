def substring(s):
    testString = ""
    count = 0
    max = 0
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            if s[j] not in testString:
                count += 1
                testString += s[j]
            else:
                break
        if count > max:
            max = count
        count = 0
        testString = ""        
    
    return max