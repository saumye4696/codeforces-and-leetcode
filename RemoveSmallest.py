def remove():
    t = int(input())
    final = []
    
    for i in range(t):
        n = int(input())
        l = [None] * n
        l = list(map(int, input().split()))
        l.sort()
        flag = True
        if len(l) == 1:
            flag = False    
        for i in range(len(l)-1):
            if l[i+1] - l[i] > 1:
                flag = False
                break
            else:
                flag = True
                
            final.append("YES")
        else:
            final.append("NO")

    return final

print(remove())
