from datetime import datetime
class MonHoc:
    def __init__(self,ma,maP,ten,date,tg,sh ):
        self.ma= "T"+"{:03d}".format(ma)
        self.maP = maP
        self.ten = ten
        self.date =  datetime.strptime(date,'%d/%m/%Y')
        self.tg = tg
        self.sh = sh

def formattedDate(tmp):
    tmp = str(tmp)[:10]
    tmp = tmp. split('-')
    tmp = ''+tmp[2] + "/"+tmp[1]+'/'+tmp[0]
    return tmp
n,m = map(int,input().split())
mon = {}
for i in range(n):
    key = input()
    value = input()
    mon[key] = value
CacMon = []
for i in range(m):
    s = input().split()
    key = s[0]
    CacMon.append(MonHoc(i+1 , s[0],mon[key] ,s[1] ,s[2],s[3]))
CacMon.sort(key=lambda x : (x.date,x.tg,x.maP))
for monHoc in CacMon:
    print(f"{monHoc.ma} {monHoc.maP} {monHoc.ten} {formattedDate(monHoc.date)} {monHoc.tg} {monHoc.sh}")
