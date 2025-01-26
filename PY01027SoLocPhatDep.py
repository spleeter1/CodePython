n = input()
ok = 1
a = '6'
b = '68'
c = '688'
if '6' in n or '68' in n or '688' in n:
    ok = 1
else:
    ok = 0
for i in range(0,len(n)):
    if n[i] != '6' and n[i] != '8':
        ok = 0
print("YES") if ok == 1 else print("NO")
    