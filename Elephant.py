def elephant(x):
    count = 0
    n = x
    for i in range(5,0,-1):
        count += n//i
        n = n % i
    print(count)
    
x = int(input())
elephant(x)