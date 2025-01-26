bills = []
for _ in range(int(input())):
    ma = input()
    ten = input()
    slg = int(input())
    dongia = int(input())
    chietkhau = int(input())
    tong = dongia*slg - chietkhau
    bills.append((ma,ten,slg,dongia,chietkhau,tong))

bills.sort(key=lambda x : -x[5])
for bill in bills:
    print(bill[0],bill[1],bill[2],bill[3],bill[4],bill[5])
