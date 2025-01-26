N, M = map(int, input().split())
A = []
max_palindrome = -1
positions = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for i in range(N):
    for j in range(M):
        num = A[i][j]
        reverse_num = int(str(num)[::-1])
        if num >= 10 and num == reverse_num and num > max_palindrome:
            max_palindrome = num
            positions = [(i, j)]
        elif num == max_palindrome:
            positions.append((i, j))

if max_palindrome != -1:
    print(max_palindrome)
    for pos in positions:
        print("Vi tri ["+str(pos[0])+"]["+ str(pos[1])+"]")
else:
    print("NOT FOUND")