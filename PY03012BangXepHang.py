sv = {}

for _ in range(int(input())):
    ten = input().strip()
    c,t = list(map(int,input().split()))
    sv[ten] = (c,t)

# print(sv)
for x in sv:
    print(sv.values())
print(type(sv))
sorted_sv = sorted(sv.items(),key = lambda tmp: (-tmp[1][0],tmp[1][1] , tmp[0]))
print(type(sorted_sv))
print(sorted_sv)
for tmp in sorted_sv:
    print(tmp[1][1])
    # print(f'{tmp[0]} {tmp[1][0]} {tmp[1][1]}')
    

