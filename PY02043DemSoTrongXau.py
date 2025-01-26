for j in range(int(input())):
    n = input()
    k = input()
    cnt =0
    i=0
    while i < len(n) - len(k) + 1:
        if n[i:i + len(k)] == k:
           # print(i, "", n[i:i + len(k)], " ", k)
            cnt += 1
            i += len(k)
        else:
            i += 1
    print(cnt)