def tong_diem(kv,diem,dtoc):
    if kv==1:    diem+=1.5
    elif kv==2: diem+=1
    if dtoc != 'Kinh':
        diem += 1.5
    return diem
def mon(s):
    if s[0] == 'A': return 'TOAN'
    elif s[0] == 'B': return 'LY'
    else:   return'HOA'
thisinh = []
for i in range(int(input())):
    ma = "TS"+"{:02d}".format(i+1)
    name = input()
    name = (" ").join(name.lower().split()).title()
    diem = float(input())
    dtoc = input()
    kv = int(input())
    diem = tong_diem(kv,diem,dtoc)
    status = 'Do' if diem >=20.5 else 'Truot'
    thisinh.append((ma,name,diem,status))
ans = sorted(thisinh,key=lambda x: (-x[2],x[0]))
for i in ans:
    print(f"{i[0]} {i[1]} {i[2]} {i[3]}" )
