for i in range(0,int(input())):
    n = input()
    tong = 0
    for j in n:
        tong+=int(j)
    if str(tong) == str(tong)[::-1] and tong>9:
        print("YES")
    else:
        print("NO")