n = int(input())
def calcPrice(n):
    if n>100:
        return round((50*100 + 50*150 + (n-100)*200)*1.05)
    elif n>50:
        return round((50*100 + (n-50)*150)*1.03)
    else:
        return round(n*100*1.02)
HoaDon = []
for i in range(n):
    name = input()
    numOld = int(input())
    numNew = int(input())
    code = "KH"+str(i+1).zfill(2)
    total = calcPrice(numNew-numOld)
    HoaDon.append((code,name,total))

HoaDon.sort(key=lambda x: (-x[2]))
for hd in HoaDon:
    code,name,ans = hd
    print(f"{code} {name} {ans}")
