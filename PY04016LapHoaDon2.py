import datetime
def tp(s):
    x = s[0]
    if x == '1': return 25
    elif x == '2': return 34
    elif x== '3' :return 50
    else: return 80

bills = []
date_format = "%d/%m/%Y"
for i in range(int(input())):
    ma = "KH" + "{:02d}".format(i+1)
    ten = input()
    room = input()
    tien1ngay = tp(room)
    vao = input().strip()
    vao = datetime.datetime.strptime(vao,date_format)
    ra = input().strip()
    ra = datetime.datetime.strptime(ra,date_format)
    ngay = (ra - vao).days
    if ngay ==0 : ngay = 1
    else:
        ngay+=1
    them = int(input())
    tongtien = tien1ngay*ngay + them
    bills.append((ma,ten,room,ngay,tongtien))
bills.sort(key=lambda x : -x[4])
for bill in bills:
    print(bill[0], bill[1], bill[2], bill[3], bill[4])
