t = int(input())
mon = []
for _ in range(t):
    ma = input().strip()
    ten = input().strip()
    ht = input().strip()
    mon.append((ma,ten,ht))

mon.sort(key=lambda x: (x[0]))
for tmp in mon:
    print(tmp[0]+" "+tmp[1]+" "+tmp[2])
