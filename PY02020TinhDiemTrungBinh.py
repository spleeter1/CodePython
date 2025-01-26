n = int(input())

a = [float(i) for i in input().split()]

smax = 0
smin =99999
for i in a:
    if i>smax:
        smax = i
    elif i<smin:
        smin = i

for i in a:
    if i == smax or i == smin:
        a.remove(i)
tong = 0
for i in a:
    tong+=i
print(round(tong/len(a),2))
