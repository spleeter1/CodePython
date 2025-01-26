n = input()
ok = 0
for j in range(0,int(n)):
    ok=0
    k = input()
    for i in range (0,len(k)):
        if k[i] !='4' and k[i] != '7':
            print("NO")
            ok = 1
            break
    if ok ==0:
        print("YES")