for _ in range(int(input())):
    n = input()
    i=0
    a = []
    tmp = ""
    ok = 1
    while i<len(n):
        if ord(n[i]) >= 48 and ord(n[i]) <= 57:    
            tmp+=n[i]
            ok = 1
        else:
            a.append(tmp)
            tmp = ""
            ok = 0
        if ok == 0 or (i==len(n)-1 and ok ==1):
            a.append(tmp)
        i+=1
    
    while  "" in a:
        a.remove("")
    #print(a)
    smax = 0
    for j in a:
        if smax < int(j):
            smax = int(j)
    print(smax)