for i in range(int(input())):
    n = input()
    ok = 1
    for j in range(0,len(n)-2):
        if n[j] != n[j+2]:
            ok=0
            break
    print("YES") if ok == 1 else print("NO")
        