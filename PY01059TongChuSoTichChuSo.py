for j in range(int(input())):
    n = input()
    tong = 0
    tich = 1
    ok=0
    for i in range(0,len(n)):
        if(i%2==0):
            tong+=int(n[i])
        elif int(n[i])!=0:     
            tich*=int(n[i])
            ok = 1
    print ( tong,end=" ")
    print(tich) if ok == 1 else print("0")
