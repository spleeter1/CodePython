for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    cnt = [0]*100005
    for i in a:
        cnt[i]+=1
    if 1 in cnt:
        print("YES")
    else:
        print("NO")
