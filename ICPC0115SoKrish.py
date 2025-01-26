a = [1]
tich = 1
for i in range(1,10): 
    tich *=i
    a.append(tich)

for _ in range(int(input())):
    n = input()
    tong = 0
    for i in range(len(n)):
        tong+=a[int(n[i])]

    if tong == int(n):
        print("Yes")
    else:
        print("No")
    