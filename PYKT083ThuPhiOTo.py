def tinhtien(loai,ghe):
    if loai =='Xe_con':
        if ghe == '5':
            return 10000
        else: return 15000
    elif loai =='Xe_tai':
        return 20000
    else:
        if ghe == '29': return 50000
        else: return 70000
n = int(input())
date = {}
for i in range (n):
    inpt = input().split()
    tien = 0
    if inpt[3] == 'IN':
        if inpt[4] in date:
            date[inpt[4]]+= tinhtien(inpt[1],inpt[2])
        else:
            date[inpt[4]] = tinhtien(inpt[1],inpt[2])
keys = list(date.keys())
keys.sort()
for i in keys:
    print(f"{i}: {date[i]}")