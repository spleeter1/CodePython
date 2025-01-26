def convert(time):
    a=time.split(':')
    return int(a[0])*60+int(a[1])
def getMa(ten,diadiem):
    s =""
    for i in diadiem:
        s+=i[0]
    for i in ten:
        s+=i[0]
    return s
def vtoc(tg):
    return (120/((tg-360)/60))
n = int(input())
vdv = []
for i in range(n):
    ten = input().split()
    diadiem = input().split()
    vt = vtoc(convert(input()))
    # print(ten,diadiem)
    ma = getMa(ten,diadiem)
    vdv.append((ma , ten , diadiem, vt))
vdvTmp = sorted(vdv,key=lambda x : -x[3])
for i in vdvTmp:
    ten = " ".join(i[1])
    tinh = " ".join(i[2])
    print(f"{i[0]} {ten} {tinh} {round(i[3])} Km/h")