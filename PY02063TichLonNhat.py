# n = int(input())
# a = [int(i) for i in input().split()]
# a.sort()
# l = len(a)
# ans = 0
# res = a[0] * a[1]
# if ans < res:
#     ans = res
# res = a[l-1] * a[l-2] * a[l-3]
# if ans <res:
#     ans = res
# res = a[l-1] * a[l-2] 
# if ans<res:
#     ans = res
# res = a[0] * a[1] * a[2]
# if ans<res:
#     ans = res
# print(ans)

# Bài này lỗi vì cho test 
# 5
# 0 -1 -2 -3 -4 
# code 1 đúng hơn :)
n = input()
a = list(map(int, input().split()))

max1 = max2 = max3 = -10000
min1 = min2 = 10000

for i in a:
    if i >= max1:
        max3 = max2
        max2 = max1
        max1 = i
    elif i >= max2:
        max3 = max2
        max2 = i
    elif i > max3:
        max3 = i
    if i <= min1:
        min2 = min1
        min1 = i
    elif i < min2:
        min2 = i

print(max(max1 * max2 * max3, max1 * min1 * min2))