def xuly(s):
    diem = 10
    for i in range(len(s)):
        if s[i]== 'v':
            diem-=2
        elif s[i] == 'm':
            diem-=1
    if diem < 0:
        return 0
    else:
        return diem
n = int(input())
sv = {}
for i in range(n):
    msv = input()
    ten = input()
    lop = input()
    sv[msv] = {"ten": ten,'lop': lop}

for i in range(n):
    msv,check = input().split()
    diem = xuly(check)
    if msv in sv:
        sv[msv]["diem"] = diem
for msv,info in sv.items():
    if info["diem"] == 0:
        print(f"{msv} {info['ten']} {info['lop']} {info['diem']} KDDK")
    else:
        print(f"{msv} {info['ten']} {info['lop']} {info['diem']}")
