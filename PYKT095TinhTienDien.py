def rename(s):
    return " ".join(s.lower().split()).title()
def loai(s):
    if s == 'A':return 100
    elif s =='B':return 500
    else: return 200
def tienDm(dmuc,sDien):
    if sDien <= dmuc:   return sDien*450
    else: return dmuc*450
def tienVuot(dmuc,sDien):
    if sDien>dmuc:
        return (sDien-dmuc)*1000
    return 0
def vat(x):
    return x//20
bills = []
for i in range(int(input())):
    ma = "KH"+"{:02d}".format(i+1)
    name = input()
    s = input().split()
    dmuc = loai(s[0])
    soDien = int(s[2]) - int(s[1])
    tong = tienDm(dmuc,soDien)+tienVuot(dmuc,soDien)+vat(tienVuot(dmuc,soDien))
    bills.append((ma,rename(name),tienDm(dmuc,soDien),tienVuot(dmuc,soDien),vat(tienVuot(dmuc,soDien)),tong))
bills.sort(key=lambda x : -x[5])
for i in bills:
    print(i[0],i[1],i[2],i[3],i[4],i[5])