def kt(n):
    if n == n[::-1]:
        return True
    else:
        return False
n = input()
cd = len(n)
lenmax=0
for i in range(0,cd):
