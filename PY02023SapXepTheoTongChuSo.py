def cal(n):
    res = 0
    for i in range (len(n)):
        res+=int(n[i])
    return res


for _ in range (int(input())):
    n = int(input())
    inpt = [str(i) for i in input().split()]
    res = []
    for i in range(len(inpt)):
        res.append((cal(inpt[i]),int(inpt[i])))
    res.sort()
    for i in range(len(inpt)):
        print(res[i][1],end=" ")
    print()