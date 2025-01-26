# a, n = [], int(input())
# for i in range(n): 
#     a.append(int(input()))

# def low(arr, L, x):
#     R = len(arr)-1
#     while L<R:
#         mid = (L+R)>>1
#         if arr[mid]<x: L = mid+1
#         else: R = mid
#     return L

# z = sorted(set(a))
# m = [[] for i in z]
# first = [0]*len(z)

# for i in range(n):
#     a[i] = low(z, 0, a[i])
#     m[a[i]].append(i)

# def get(arr, start, end, step, root):
#     st = [] 
#     for i in range(start, end, step):
#         while len(st)>0 and a[st[-1]] <= a[i]: st.pop()
#         arr[i] = root if len(st)==0 else st[-1]
#         st.append(i)

# l, r = [0]*n, [0]*n
# get(l, 0, n, 1, -1)
# get(r, n-1, -1, -1, n)

# def count(arr, start, end):
#     if start >= len(arr) or end < arr[start]: return 0
#     pos = low(arr, start, end)
#     if arr[pos] > end: pos-=1
#     return pos - start + 1
# s = 0
# for i in range(n):
#     if l[i]!=-1: s+=1
#     if r[i]!=n: s+=1
#     x = count(m[a[i]], first[a[i]], r[i] - 1)
#     s += (x-1)*x//2
#     first[a[i]]+=x

# print(s)

# import sys
# input = sys.stdin.readline

# class SegmentTree:
#     def __init__(self, n):
#         self.n = n
#         self.tree = [0] * (n << 2)

#     def update(self, node, start, end, index, value):
#         if start > index or end < index:
#             return
#         if start == end:
#             self.tree[node] = value
#             return
#         mid = (start + end) >> 1
#         self.update(node << 1, start, mid, index, value)
#         self.update(node << 1 | 1, mid + 1, end, index, value)
#         self.tree[node] = self.tree[node << 1] + self.tree[node << 1 | 1]

#     def query(self, node, start, end, left, right):
#         if start > right or end < left:
#             return 0
#         if left <= start and end <= right:
#             return self.tree[node]
#         mid = (start + end) >> 1
#         return self.query(node << 1, start, mid, left, right) + self.query(node << 1 | 1, mid + 1, end, left, right)

# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# freq = {}
# for num in arr:
#     freq[num] = freq.get(num, 0) + 1
# indices = {num: [] for num in freq}
# for i, num in enumerate(arr):
#     indices[num].append(i)

# seg = SegmentTree(n)
# for i, num in enumerate(arr):
#     seg.update(1, 0, n - 1, i, freq[num])

# ans = 0
# for num, ind in indices.items():
#     for i in range(len(ind)):
#         left = ind[i]
#         right = ind[i + 1] - 1 if i + 1 < len(ind) else n - 1
#         ans += seg.query(1, 0, n - 1, 0, num - 1) * (ind[i + 1] - ind[i] if i + 1 < len(ind) else n - left)
#         seg.update(1, 0, n - 1, left, freq[num] - 1)
# print(ans)

# from sys import stdin
# input = stdin.readline
# a, n = [], int(input())
# for i in range(n): a.append(int(input()))

# def low(arr, L, x):
#     R = len(arr)-1
#     while L<R:
#         mid = (L+R)>>1
#         if arr[mid]<x: L = mid+1
#         else: R = mid
#     return L

# z = sorted(set(a))
# m = [[] for i in z]
# first = [0]*len(z)

# for i in range(n):
#     a[i] = low(z, 0, a[i])
#     m[a[i]].append(i)

# def get(arr, start, end, step, root):
#     st = [] 
#     for i in range(start, end, step):
#         while len(st)>0 and a[st[-1]] <= a[i]: st.pop()
#         arr[i] = root if len(st)==0 else st[-1]
#         st.append(i)

# l, r = [0]*n, [0]*n
# get(l, 0, n, 1, -1)
# get(r, n-1, -1, -1, n)

# def count(arr, start, end):
#     if start >= len(arr) or end < arr[start]: return 0
#     pos = low(arr, start, end)
#     if arr[pos] > end: pos-=1
#     return pos - start + 1
# s = 0
# for i in range(n):
#     if l[i]!=-1: s+=1
#     if r[i]!=n: s+=1
#     x = count(m[a[i]], first[a[i]], r[i] - 1)
#     s += (x-1)*x//2
#     first[a[i]]+=x

# print(s)
from sys import stdin

input = stdin.readline

# Đọc số lượng phần tử
n = int(input())

# Đọc danh sách các phần tử
arr =[]
for i in range(n): 
    arr.append(int(input()))

# Tạo một ngăn xếp để lưu trữ chỉ mục của các phần tử
stack = []

# Khởi tạo biến đếm cặp
count_pairs = 0

# Duyệt qua danh sách các phần tử
for i in range(n):
    # Làm rỗng ngăn xếp cho đến khi gặp một phần tử lớn hơn hoặc bằng phần tử hiện tại
    while stack and arr[i] >= arr[stack[-1]]:
        # Lấy chỉ mục của phần tử khỏi ngăn xếp
        top = stack.pop()
        # Tính toán số cặp mới mà phần tử tại chỉ mục top là một phần tử lớn nhất
        count_pairs += i - top - 1 if stack else 0
    # Thêm chỉ mục của phần tử hiện tại vào ngăn xếp
    stack.append(i)

# Tính toán số cặp cho các phần tử còn lại trong ngăn xếp
while stack:
    top = stack.pop()
    count_pairs += len(stack)

# In ra số lượng cặp
print(count_pairs)
