def magnets():
    n = int(input())
    # l = list(map(int,input().split()))
    l = [None] * n
    for i in range(n):
        l[i] = int(input())

    temp = l[0]
    g = 1
    
    for i in range(len(l)-1):
        temp = l[i]
        if temp != l[i+1]: 
            g += 1
    
    return g    

print(magnets())