n = input()
ok = 0
for j in range(0,int(n)):
    ok=0
    k = input()
    if k[(len(k)-2):] == "86":
        print("YES")
    else:
        print("NO")