n = input()
for i in range(0,int(n)):
    so = input()
    j = 1
    cd = len(so)
    ok = 1
    if len(so)< 3:
        ok =2
    while j<cd:
        if ok == 1 and so[j] < so[j-1]:
            ok=0
        elif ok==1 and so[j] == so[j-1]:
            ok = 2
            break
        elif ok == 0 and so[j] > so[j-1]:
            ok =2
            break
        j+=1
    if ok !=2 :
        print("YES")
    else:
        print("NO")