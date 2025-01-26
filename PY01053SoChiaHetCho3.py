for i in range(0,int(input())):
    n = input()
    tong = 0
    for j in n:
        tong+=int(j)
    if tong%3==0:
        print("YES")
    else:
        print("NO")