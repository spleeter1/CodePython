for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    cnt = {}
    dk = n//2
    cntmax = 0
    smax = 0
    for i in a:
        if i in cnt:
            cnt[i] +=1
        else:
            cnt[i] = 1
        if cnt[i] > cntmax:
            cntmax = cnt[i]
            smax = i
    if cnt[smax] > dk:
        print(smax)
    else:
        print("NO")         