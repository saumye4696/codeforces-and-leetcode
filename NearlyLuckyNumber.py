def lucky():
    n = int(input())
    num = n
    count = 0
    while(n > 0):
        dig = n % 10
        if(dig == 4 or dig == 7):
            count += 1
        n = n // 10
    k = count
    c = 0
    while(count > 0):
        d = count % 10
        if(d == 4 or d == 7):
            c += 1
        if(c == len(k)):
            print("YES")
        else:
            print("NO")

lucky()    