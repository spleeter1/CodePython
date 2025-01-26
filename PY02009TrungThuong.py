for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        tmp = int(input())
        a.append(tmp)

    cnt = {}
    for i in a:
        if i in cnt:
            cnt[i]+=1
        else:
            cnt[i]=1

    a.sort()
    cntmax = 0
    smax = 0
    for i in a:
        if cnt[i] >cntmax:
            cntmax = cnt[i]
            smax = i
    print(smax)
        