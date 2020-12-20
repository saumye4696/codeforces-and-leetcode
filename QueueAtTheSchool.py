def queue():
    n, t = map(int, input().split())
    s1 = input()
    str1 = ""
    s = list(s1)
    while(t):
        for i in range(1, n):
            if(s[i] == 'G' and s[i-1] == 'B'):
                s[i] = 'B'
                s[i-1] = 'G'
                i += 1
        t -= 1
    for i in range(len(s)):
        str1 += s[i]
    print(str1)

queue()