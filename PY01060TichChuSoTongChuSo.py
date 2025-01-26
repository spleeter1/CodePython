for j in range(int(input())):
    n = input()
    tich = 1
    tong = 0
    ok=0
    for i in range(0,len(n)):
        if(i%2!=0):
            tong+=int(n[i])
        elif int(n[i])!=0:     
            tich*=int(n[i])
            ok = 1
    print   (tich,end=" ") if ok == 1 else print("0",end=" ")
    print(tong)
