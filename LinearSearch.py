def linear(arr, num):
    for i in arr:
        if num == i :
            return True
    return False
l1 = [1,2,3,4,5,6,7,8,9]
if(linear(l1, 25)):
    print("FOUND")
else:
    print("NOT FOUND")