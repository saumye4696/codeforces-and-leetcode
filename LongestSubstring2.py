def substring(s):
    testString = ""
    count = 0
    max = 0
    start = 0
    for i in range(len(s)):
        start += 1
        if s[i] not in testString:
            testString += s[i]
            count += 1
        else:
            break
        if count > max:
            max = count