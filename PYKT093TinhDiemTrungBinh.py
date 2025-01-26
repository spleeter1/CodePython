from decimal import Decimal,ROUND_HALF_UP
n = int(input())
sv = []
for i in range(n):
    ma = 'SV' + "{:02d}".format(i+1)
    ten = (" ").join(input().strip().lower().split()).title()
    a = int(input()) *3
    b = int(input()) *3
    c = int(input()) *2
    ans = (a+b+c)/8
    ans = Decimal(ans)
    ans = ans.quantize(Decimal('0.00') , rounding= ROUND_HALF_UP)
    sv.append([ma,ten,ans])
sv.sort(key=lambda x : -x[2])
# print(sv)
i = 0
j = 1
rank = [1]*len(sv)
while i< len(sv):
    j=i+1
    if i > 0:   rank[i] = rank[i-1] +dem +1
    rank[0] = 1
    dem = 0
    
    while j< len(sv) and sv[i][2] == sv[j][2] : 
        rank[j] = rank[i]
        j+=1
        dem += 1
    i+=dem
    i+=1
# print(rank)
cnt = 0
for i in sv:
    print(i[0],i[1],i[2],rank[cnt])
    cnt +=1
