from datetime import datetime
with open("MONTHI.in",'r') as f:
    data = f.readlines()

t = int(data[0].strip())
idx = 1
mon = {}
for _ in range (t):
    mon[data[idx].strip()] = data[idx+1].strip()
    idx+=3
# print(mon)

with open("CATHI.in",'r') as f:
    data = f.readlines()

t = int(data[0].strip())
idx = 1
caThi = []
for _ in range(t):
    ngay = data[idx].strip()
    gio = data[idx+1].strip()
    phong = int(data[idx+2].strip())
    tg = f"{ngay} {gio}"
    timeStamp = datetime.strptime(tg,'%d/%m/%Y %H:%M')
    caThi.append((ngay,gio,phong,timeStamp))
    idx+=3

with open("LICHTHI.in",'r') as f:
    data = f.readlines()

t = int(data[0].strip())
idx = 1
lichThi = []
for i in range(t):
    ma = data[idx].strip().split()[0]
    ma_mon = data[idx].strip().split()[1]
    nhom = data[idx].strip().split()[2]
    slg = data[idx].strip().split()[3]
    idx+=1
    lichThi.append((caThi[i],mon[ma_mon],nhom,slg,ma))
    # print(lichThi)

lichThi.sort(key=lambda x: (x[0][3],x[4]))

for x in lichThi:
    print(f'{x[0][3].strftime("%d/%m/%Y %H:%M")} {str(x[0][2]).strip()} {x[1].strip()} {str(x[2]).strip()} {str(x[3]).strip()}')