for i in range(0,int(input())):
    n = input()
    tich = 1
    for j in n:
        if int(j) != 0:
            tich*=int(j)
    print(tich)
   