def xulyDiem(s):
    if s == '10':
        return float(10)
    if "." in s:
        return float(s)
    else:
        return float(s[0]+'.'+s[1:])
    
def Loai(diem):
    if diem >=9.5:
        return 'XUAT SAC'
    elif diem>=8:
        return 'DAT'
    elif diem>=5:
        return 'CAN NHAC'
    else:
        return 'TRUOT'

n = int(input())
ThiSinh = []
for i in range(n):
    ma = 'TS0'+str(i+1)
    ten = input()
    diem1 = input()
    diem2 = input()
    TinhDiem = (xulyDiem(diem2) + xulyDiem(diem1))/2
    kq = Loai(TinhDiem)
    ThiSinh.append((ma,ten,TinhDiem,kq))

ThiSinh.sort(key=lambda x:  -x[2])
for ts in ThiSinh:
    print ('{} {} {:.2f} {}'.format(ts[0],ts[1],ts[2],ts[3]))
