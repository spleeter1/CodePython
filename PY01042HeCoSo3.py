for i in range(int(input())):
    n = input()
    ok = 1
    for j in range(0,len(n)):
        if n[j] != '1' and n[j] != '2' and n[j] != '0':
            ok=0
            break
    print("YES") if ok == 1 else print("NO")
        