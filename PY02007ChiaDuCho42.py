# a = []
# cnt=0
# while len(a)<10:
#     n = input().split()
#     for i in n:
#         a.append(int(i))
#         if len(a) >= 10:
#             break
    
# for i in range (len(a)):
#     if a[i] % 42 !=0:
#         cnt+=1
# print(cnt)

dd = [0] * 42
cnt, res = 10, 0
while cnt != 0:
    a = [int(i) for i in input().split()]
    cnt -= len(a)
    for i in a:
        if dd[i % 42] == 0:
            dd[i % 42] = 1
            res += 1
print(res)