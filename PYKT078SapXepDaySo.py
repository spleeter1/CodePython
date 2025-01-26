for _ in range (int(input())):
    n,m = map(int,input().split())
    a = [int(i) for i in input().split()]
    sa = []
    sd = []
    ans = []
    cnt = 0
    smax = max(a)
    for i in range(len(a)):
        if a[i] == smax:
            a.insert(i,m)
            break
    for i in range(len(a)):
        if a[i] < 0:
            sa.append(a[i])
        else:
            sd.append(a[i])
    ans.extend(sa)
    ans.extend(sd)
    for i in range(len(ans)):
        print(ans[i],end=" ")  
    print()  