def money():
    # k = int(input())
    # n = int(input())
    # w = int(input())
    k,n,w = int(input())
    for i in range(0,w):
        sum += i*k
    if(sum <= n):
        print(0)
    else:
        print(sum - n)

money()