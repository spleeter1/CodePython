def tcs(n):
    tong = 0
    for i in range(0, len(n)):
        tong += ord(n[i]) - ord('0')  # Chuyển ký tự thành giá trị số nguyên
    return tong

n = input()
cnt = 1
tong = tcs(n)
while tong >= 10:
    res = str(tong)
    tong = tcs(res)
    cnt += 1

print(cnt)