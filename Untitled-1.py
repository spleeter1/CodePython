
dic = {}
n, m = input().split()
n = int(n)
m = int(m)
for i in range (0,n):
    tl = input()
    dic[tl] = "TL00"+str(i+1)
# print(dic.values())
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)
film = []
for i in range(0,m):
    ma = "P00"+str(i+1)
    # print(ma)
    ngay = input()
    ten = input()
    tap = input()
    loai = dic[ten]
    # print(loai)
    film.append((ma,loai,ngay,ten,tap))
    print(film[i])
