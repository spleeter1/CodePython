def tong_diem(s,diem):
    x = s[1]
    if x=='1':    diem+=2
    elif x=='2': diem+=1.5
    elif x=='3': diem+=1
    return diem
def mon(s):
    if s[0] == 'A': return 'TOAN'
    elif s[0] == 'B': return 'LY'
    else:   return'HOA'
thisinh = []
for i in range(int(input())):
    ma = "GV"+"{:02d}".format(i+1)
    name = input()
    diem_cong = input()
    monh = mon(diem_cong)
    diem1 = float(input())
    diem2 = float(input())
    diem = diem1*2 +diem2
    diem = tong_diem(diem_cong,diem)
    status = 'TRUNG TUYEN' if diem >=18 else 'LOAI'
    thisinh.append((ma,name,monh,diem,status))
ans = sorted(thisinh,key=lambda x: -x[3])
for i in ans:
    print(f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]}" )
