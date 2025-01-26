for i in range(int(input())):
    n = input()
    tong=int(n[0])
    ok=1
    for j in range (1,len(n)):
        tong+=int(n[j])
        if(abs(int(n[j]) - int(n[j-1])) != 2):
            ok=0
            break
    if ok == 1 and tong%10==0:
        print("YES")
    else:
        print("NO")