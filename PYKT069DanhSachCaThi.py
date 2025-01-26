from datetime import datetime

with open("CATHI.in",'r') as f:
    data = f.readlines()

#t = int(input())
t = int(data[0].strip())
caThi = []
idx = 1
for i in range(0,t):
    ma = 'C'+"{:03d}".format(i+1)
    # print(ma)
    ngay = data[idx].strip()
    gio = data[idx+1].strip()
    phong = int(data[idx+2].strip())
    idx += 3
    datetime_str = f"{ngay} {gio}"
    datetime_obj = datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")
    # print("ngay: ",datetime_obj)
    caThi.append((ma,datetime_obj,ngay,gio,phong))

caThi.sort(key=lambda x: (x[1],x[0]))
for x in caThi:
    print(f"{x[0]} {x[2]} {x[3]} {x[4]}")
